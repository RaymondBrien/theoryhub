from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from quiz.models import Quiz
from .models import UserQuizSubmission, QuizNote

def dashboard(request, username):
    """
    Context 
    Template
    
    """
    user = get_object_or_404(User, username=username)
    submissions = UserQuizSubmission.objects.filter(owner=user) 
    return render(request, 'dashboard/dashboard.html', {'submissions': submissions, 'user': user})

    # # TODO get any notes made related to a quiz from user in notepad and display on quiz list page
    # def get_context_data(self, **kwargs): # ensure quiz note form shows
    #     context = super().get_context_data(**kwargs)
    #     context['quiz_note_form'] = QuizNoteForm()
    #     return context
    

def quiz_note(request, slug):
    """
    View to display a single quiz note.

    Context:
        quiz: single instance of :model:`quiz.Quiz`
        quiz_note: single instance of :model:`quiz.QuizNote`
    
    **Template**
        quiz_note TODO make quiz note template
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
        'quiz/single_quiz.html',
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
    
    