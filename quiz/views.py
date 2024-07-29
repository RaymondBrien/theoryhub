from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from django.http import HttpResponseRedirect
from django.db.models import Prefetch
from django.contrib.auth.models import User

from .models import Quiz, Question, Answer, QuizNote
from .forms import AnswerSelection, QuizNoteForm
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
    
    def get_context_data(self, **kwargs): # ensure quiz note form shows
        context = super().get_context_data(**kwargs)
        context['quiz_note_form'] = QuizNoteForm()
        return context

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


def quiz_note(request, slug):
    """
    View to display a single quiz note.

    Context:
        quiz: single instance of :model:`quiz.Quiz`
        quiz_note: single instance of :model:`quiz.QuizNote`

    Template:
        dashboard/quiz_note.html
    """
    queryset = Quiz.objects.filter(status=1)
    quiz= get_object_or_404(queryset, slug=slug)
    quiz_notes = quiz.quiz_notes.all().order_by("-created_at")
    if request.method == "POST":
        quiz_note_form = QuizNoteForm(data=request.POST)
        if quiz_note_form.is_valid():
            quiz_note = quiz_note_form.save(commit=False)
            quiz_note.user = request.user
            quiz_note.quiz = quiz
            quiz_note.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Quiznote added'
            )
    
    quiz_note_form = QuizNoteForm() 
    return render(
        request, 
        'quiz/quiz_note.html',
        {
        'quiz': quiz,
        'quiz_notes': quiz_notes,
        'quiz_note_form': quiz_note_form
    },
)

# TODO: debug if quiznote_id not correct param
@login_required
def edit_quiz_note(request, slug, quiznote_id):
    """
    Display individual quiznote for user to edit if authenticated:
    Stays on page after the edit is submitted.
    
    **Context** 
    `quiz` - single instance of Quiz object (published only)
    `quiz_note` - single instance of quiz note object, related to quiz via FK.
    
    Appears on quiz list template.
    """
    if request.method == "POST":
        queryset = Quiz.objects.filter(status=1)
        quiz = get_object_or_404(queryset, slug=slug)
        quiz_note = get_object_or_404(QuizNote, pk=quiznote_id) # debug needed here?
        quiz_note_form = QuizNoteForm(data=request.POST, instance=quiz_note)
        
        if quiz_note_form.is_valid() and quiz_note.user == request.user:
            quiz_note = quiz_note_form.save(comment=False)
            quiz_note.quiz = quiz
            quiz_note.save()
            messages.add_message(request, messages.SUCCESS, 'Quiz note updated!')
        else: 
            messages.add_message(request, messages.ERROR, 'Error updating quiznote!')
    
    # TODO where do I want to stay on page?
    return HttpResponseRedirect(reverse('quiz_list'))
  
 
def delete_quiz_note(request, slug, quiznote_id):
    """
    Enables user to delete a quiz note instance.
    
    **Context**
    
    `quiz` - single instance of Quiz object, published only
    `quiz_note` - single instance of quiznote object, attached to quiz via FK.
    
    Appears on quiz list template.
    """
    
    queryset = Quiz.objects.filter(status=1)
    quiz = get_object_or_404(queryset, slug=slug)
    quiz_note = get_object_or_404(QuizNote, pk=quiznote_id) # TODO check pk name
    
    if quiz_note.user == request.user:
        quiz_note.delete()
        messages.add_message(request, messages.SUCCESS, 'Quiznote deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'There are no quiznotes you can delete.')
    
    return HttpResponseRedirect(reverse('quiz_list')) # TODO is this correct?
    
    
