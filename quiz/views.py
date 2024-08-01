from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from django.http import HttpResponseRedirect
from django.db.models import Prefetch
from django.contrib.auth.models import User

from .models import Quiz, Question, Answer 
from .forms import AnswerSelection
from dashboard.models import UserQuizSubmission 

class QuizList(generic.ListView):
    """
    Displays a list of all quizzes in :model:`quiz.Quizzes`
    paginated by 6 quizzes per page.
    """
    queryset = Quiz.objects.filter(status=1) #  only display published quizzes
    template_name = 'quiz/quiz_list.html'
    paginate_by = 6
    context_object_name = 'quiz_list'

    

@login_required
def single_quiz(request, slug):
    """
    Displays a single quiz with its questions.
    
    **Context**
    ``queryset`` TODO: edit params to includes slug

    **Template**
    :template:`quiz/single_quiz.html`
    
    However, there are a couple of points to note:
    """
# TODO:
# Error Handling: You might want to add some error handling around the Answer.objects.get(id=answer_id) call, in case an invalid answer ID is submitted.
# Transaction: If you're doing multiple database operations, you might want to consider using a transaction to ensure data integrity.
# Unused Code: The submit_quiz view appears to be unused and contains some inconsistencies. You might want to remove or update it if it's not being used.
    
    user = get_object_or_404(User, username=request.user)
    if not user.is_authenticated:
        messages.info(request, "Access denied. Please log in to view this page.")
        return redirect(reverse('login'))
    
    queryset = Quiz.objects.filter(status=1) 
    quiz = get_object_or_404(queryset, slug=slug)
    print(f'quiz: {quiz}')
    print(f'quiz questions: {quiz.questions.count()}')
    # answers_prefetch = Prefetch('answers', queryset=Answer.objects.all())
    questions = Question.objects.filter(quiz_id=quiz)
    # TODO tidy
    # .prefetch_related(answers_prefetch)
    # answer_form = AnswerSelection(quiz=quiz)
    
    if request.method == "POST":
        answer_form = AnswerSelection(data=request.POST, quiz=quiz) # add quiz for correct quiz fields specific to this quiz instance 
        print(f'answer_form: {answer_form}')
        print(f'POST request: {request.POST}')
        
        if answer_form.is_valid():
            score = 0
            # process all questions at once
            for question in quiz.questions.all():
                # TODO debug question_qusestion.id
                answer_id = answer_form.cleaned_data[f'question_{question.id}'] # see AnswerSelection form
                answer = Answer.objects.get(id=answer_id) # compare user answer to correct answer
                if answer.correct:
                    score +=  question.points
            
            # save quiz score to database  
            result = UserQuizSubmission.objects.create(
                # includes timestamp for multiple attempts: 
                # see dashboard.models.UserQuizSubmission
                owner=user,
                quiz=quiz,
                user_score=score,
            )
            messages.success(
                request,
                # TODO debug username message?
                f'Thank you {request.user.username}, your quiz is submitted successfully.')
            return redirect('quiz_result', result)
        # TODO add else statement for invalid form or if trying to submit on behalf of another user?
        # TODO do I handle crsf token here?
    else:
        answer_form = AnswerSelection(quiz=quiz) # pass quiz object to form for GET request to dynamically generate form fields
        print(f'GEt request: answer_form {answer_form}')
        # TODO decide on redirect or maintain on same page with form as above else statement
        #      else:
        # messages.error(request, 'Error submitting quiz. Please try again.')
    # TODO decide on redirect
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # redirect to previous page if error occurs

    context = {
        'quiz': quiz,
        'questions': questions,
        'answer_form': answer_form,
    }
    return render(request, 'quiz/single_quiz.html', context)


# TODO:  To fix this issue, you should aim to pass the answers related to each question 
# to the template in a way that they can be iterated over together. 
# One common approach is to modify the Question queryset to prefetch related Answer objects. 
# This way, you don't filter Answer objects separately but access them through their relation to 
# Question objects.

@login_required
def quiz_result(request, result):
    # TODO debug as now using result instead for cleaner handling
    # quiz = get_object_or_404(Quiz, slug=slug)
    # submission = UserQuizSubmission.objects.filter(owner=request.user, quiz=quiz).order_by('-last_taken').first()
    
    context = {
        # 'quiz': quiz,
        # 'submission': submission,
    }
    return render(request, 'quiz/quiz_result.html', context)


@login_required
def submit_quiz(request, slug):
    """
    Process quiz submission and save user score to database
    """
    
    if request.method == "POST":
        quiz = get_object_or_404(Quiz, slug=slug)
        user = get_object_or_404(User, id=request.user.id)
        answer_form = AnswerSelection(data=request.POST, instance=quiz)
        user_submission = UserQuizSubmission.objects.filter(owner=user, quiz=quiz)
        score = 0


        # TODO save score to database as UserQuizSubmission
        # TODO add question answer required to form validation and clean on form first
        
        # add question score to score if answer is correct for each question
        if answer_form.is_valid() and request.user.is_authenticated:
            for question in quiz.question.all():
                if question.answer.correct:
                    score += question.points
                else:
                    score += 0
            answer_form.save(comment=False)
            answer_form.owner = user,
            answer_form.quiz = quiz,
            answer_form.user_score = score,
            answer_form.save()
            # TODO does this save it twice?
            UserQuizSubmission.objects.create(
                owner=user,
                quiz=quiz,
                user_score=score,
            )
            messages.success(
                request, 
                f'Thank you {request.user.username}, your quiz is submitted successfully.')
            return redirect('quiz_result', quiz=quiz)
                       
    elif request.user.is_authenticated or not request.user == user:
        messages.info(request, "Access denied. Please log in to view this page.")
        return redirect('quiz_list')

    else:
        messages.error(request, 'Error submitting quiz. Please try again.')
    # TODO decide on redirect
    return HttpResponseRedirect(reverse('quiz-list'))