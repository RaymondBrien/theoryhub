from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

from .models import UserQuizSubmission, QuizNote
from .forms import QuizNoteForm

def dashboard(request, ):
    """
    Context 
    Template
    
    """
    # user = get_object_or_404(User, user=request.user)
    submissions = UserQuizSubmission.objects.filter(owner=request.user)
    return render(
        request, 
        'dashboard/dashboard.html', 
        {
            'submissions': submissions, 'user': request.user
        }
    )

    # # TODO get any notes made related to a quiz from user in notepad and display on quiz list page
    # def get_context_data(self, **kwargs): # ensure quiz note form shows
    #     context = super().get_context_data(**kwargs)
    #     context['quiz_note_form'] = QuizNoteForm()
    #     return context
    

class UserNote(generic.ListView):
    queryset = QuizNote.objects.all() # remove all later, filter by user
    template_name = 'dashboard/notes_page.html'
    paginate_by = 8
    context_object_name = 'notes_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quiz_note_form'] = QuizNoteForm()
        return context
# TODO handle edit method in class
    def post(self, request, *args, **kwargs):
        note = QuizNote.objects.filter(user=request.user)
        quiz_note_form = QuizNoteForm(data=request.POST)
        if quiz_note_form.is_valid():
            note = quiz_note_form.save(commit=False)
            note.user = request.user
            note.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Quiznote added'
            )
            return redirect('user_notes')
        return render(request, 'dashboard/notes_page.html', {'quiz_note_form': quiz_note_form})



# TODO: debug if quiznote_id not correct param
@login_required
def edit_note(request, note_id):
    """
    Display individual note for user to edit if authenticated:
    Stays on page after the edit is submitted.
    
    **Context** 
    TODO add context
    Appears on quiz list template.
    """
    if request.method == "POST":
        queryset = QuizNote.objects.filter(user=request.user)
        note = get_object_or_404(queryset, pk=note_id)
        quiz_note_form = QuizNoteForm(data=request.POST, instance=note)
        
        if quiz_note_form.is_valid() and note.user == request.user:
            note = quiz_note_form.save(commit=False) # TODO do I need this?
            note.save()
            messages.add_message(request, messages.SUCCESS, 'Note updated!')
        else: 
            messages.add_message(request, messages.ERROR, 'Error updating note!')
    
    # TODO where do I want to stay on page?
    return HttpResponseRedirect(reverse('user_notes')) 

 
def delete_note(request, note_id):
    """
    Enables user to delete a quiz note instance.
    
    **Context**
    TODO revise context
    `quiz` - single instance of Quiz object, published only
    `quiz_note` - single instance of quiznote object, attached to quiz via FK.
    
    Appears on quiz list template.
    """
    

    queryset = QuizNote.objects.filter(user=request.user)
    note = get_object_or_404(queryset, pk=note_id)
    
    if note.user == request.user:
        note.delete()
        messages.add_message(request, messages.SUCCESS, f'Note "{ note.note }" deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'There are no notes you can delete.')
    
    return HttpResponseRedirect(reverse('user_notes'))
    
    