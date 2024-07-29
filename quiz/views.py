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
    """
    
    user = get_object_or_404(User, username=request.user)
    if not user.is_authenticated:
        messages.info(request, "Access denied. Please log in to view this page.")
        return redirect(reverse('login'))
    
    queryset = Quiz.objects.filter(status=1) 
    quiz = get_object_or_404(queryset, slug=slug)
    # answers_prefetch = Prefetch('answers', queryset=Answer.objects.all())
    questions = Question.objects.filter(quiz_id=quiz)
    # .prefetch_related(answers_prefetch)
    answer_form = AnswerSelection(request.POST, quiz=quiz) # add quiz for correct quiz fields specific to this quiz instance 
    
    if request.method == "POST":
        if answer_form.is_valid():
            score = 0
            # process all questions at once
            for question in quiz.questions.all():
                answer_id = answer_form.cleaned_data[f'question_{question.id}'] # see AnswerSelection form
                answer = Answer.objects.get(id=answer_id) # compare user answer to correct answer
                if answer.correct:
                    score +=  question.points
            
            # save quiz score to database  
            UserQuizSubmission.objects.create(
                # includes timestamp for multiple attempts: 
                # see dashboard.models.UserQuizSubmission
                owner=user,
                quiz=quiz,
                user_score=score,
            )

            messages.success(request, f'Quiz submitted successfully. Your score is {score}.') # TODO style for clear UX
            # return redirect(reverse('quiz', kwargs={'slug': quiz.slug})) 
            return redirect('quiz_result', quiz_id=quiz.id)
        
        else:
            answer_form = AnswerSelection(quiz=quiz)

    context = {
        'quiz': quiz,
        'questions': questions,
        'form': answer_form,
    }
    return render(request, 'quiz/single_quiz.html', context)


# TODO:  To fix this issue, you should aim to pass the answers related to each question 
# to the template in a way that they can be iterated over together. 
# One common approach is to modify the Question queryset to prefetch related Answer objects. 
# This way, you don't filter Answer objects separately but access them through their relation to 
# Question objects.

@login_required
def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    submission = UserQuizSubmission.objects.filter(owner=request.user, quiz=quiz).order_by('-last_taken').first()
    
    context = {
        'quiz': quiz,
        'submission': submission,
    }
    return render(request, 'quiz/quiz_result.html', context)



