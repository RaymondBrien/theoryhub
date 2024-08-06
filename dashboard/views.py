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
def dashboard(request):
    """
    Displays list of all user's own quiz submissions data.
    Users must be logged in to view their data.

    **Context**
    :model: `dashboard.UserQuizSubmission`

    **Template**
    :template: `dashboard/dashboard.html`

    """
    submissions = UserQuizSubmission.objects.filter(owner=request.user)
    if not request.user.is_authenticated:
        messages.info(request, 'Access denied. Please log in to view this page.')
        return render(HttpResponseRedirect(reverse('login')))
    # TODO debug IMPORTANT - test by brute force too
    # elif request.user is not submissions.owner:
    #     messages.info(request, "You may not access someone else's submissions")
    #     return render(HttpResponseRedirect(reverse('login')))

    context = {
        'submissions': submissions,
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )

@login_required
def user_notes(request):
    """
    Display list of user's own quiz note items.
    Handles post request for new user notes made on page.

    **Context**
    :model: `dashboard.QuizNote`

    *Template**
    :template: `dashboard/notes_page.html`
    """
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
    Enables individual note instance editing on notes page using quiz note form.
    User is redirected to same page after the edit is submitted, where
    the note is updated and appears in the list.
    Edit updates content of note instance in database.

    Validation to ensure users can only edit their own notes.

    **Context**
    :model: `dashboard.QuizNote`
    :form: `dashboard.QuizNoteForm`

    **Template**
    :template: `dashboard/notes_page.html`

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

    return HttpResponseRedirect(reverse('user_notes'))

@login_required
def delete_note(request, note_id):
    """
    Enables user to delete a quiz note instance from database.
    Validation to ensure users can only delete their own notes.

    **Context**
    :model: `dashboard.QuizNote`

    **Template**
    :template: `dashboard/dashboard.html`

    """


    queryset = QuizNote.objects.filter(user=request.user)
    note = get_object_or_404(queryset, pk=note_id)

    if note.user == request.user:
        note.delete()
        messages.add_message(request, messages.SUCCESS, f'Note "{ note.note }" deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'There are no notes you can delete.')

    return HttpResponseRedirect(reverse('user_notes'))
