from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
import logging
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

from .models import UserQuizSubmission, QuizNote
from .forms import QuizNoteForm

@login_required
def dashboard(request, ):
    """
    Context 
    Template
    
    """
    # TODO check
    # user = get_object_or_404(User, user=request.user)
    submissions = UserQuizSubmission.objects.filter(owner=request.user)
    
    if not request.user.is_authenticated:
        messages.info(request, 'Access denied. Please log in to view this page.')
        return render(HttpResponseRedirect(reverse('login')))
    # TODO debug IMPORTANT - test by brute force too
    # elif request.user is not submissions.owner:
    #     messages.info(request, "You may not access someone else's submissions")
    #     return render(HttpResponseRedirect(reverse('login')))
        
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

# class UserNote(LoginRequiredMixin, UserPassesTestMixin, ListView):
#     """
#     Display all notes made by the current user.
#     Unauthenticated users will be redirected to the login page.
#     Only authenticated users can view and add notes.
#     Users can only see their own notes.
    
#     **Context**
#     TODO add more context
#     """
#     # model = QuizNote
#     template_name = 'dashboard/notes_page.html'
#     paginate_by = 8
#     context_object_name = 'notes_list'
#     # login_url = reverse('login') TODO

#     # for extra validation to avoid brute force
#     def test_func(self) -> bool | None:
#         return self.request.user.is_authenticated

#     def get_queryset(self):
#         queryset = QuizNote.objects.filter(user=self.request.user)
#         print(f'get queryset got: {queryset}')
#         return QuizNote.objects.filter(user=self.request.user)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['quiz_note_form'] = QuizNoteForm()
#         return context

#     def post(self, request, *args, **kwargs):
#         quiz_note_form = QuizNoteForm(data=request.POST)
#         if quiz_note_form.is_valid():
#             note = quiz_note_form.save(commit=False)
#             note.user = request.user
#             note.save()
#             messages.add_message(
#                 request, messages.SUCCESS,
#                 'Quiznote added'
#             )
#             return redirect('user_notes')
#         else:
#             messages.add_message(
#                 request, messages.ERROR,
#                 'Error adding quiznote'
#             )
#             return self.render_to_response(self.get_context_data(quiz_note_form=quiz_note_form))


@login_required
def user_notes(request):
    if request.method == 'POST':
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
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error adding quiznote'
            )
    else:
        quiz_note_form = QuizNoteForm()

    notes_list = QuizNote.objects.filter(user=request.user)
    
    context = {
        'notes_list': notes_list,
        'quiz_note_form': quiz_note_form,
    }
    
    return render(request, 'dashboard/notes_page.html', context)


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

@login_required
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
    
    