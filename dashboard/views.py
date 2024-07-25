from django.shortcuts import render, get_object_or_404, redirect
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


def quiz_note(request, user, slug):
    """
    View to display a single quiz note.

    Context:
        user: single instance of :model:`auth.User`
        quiz_note: single instance of :model:`dashboard.QuizNote`
        quiz: single instance of :model:`quiz.Quiz`

    Template:
        dashboard/quiz_note.html
    """
    user = get_object_or_404(User, username=user)
    quiz= get_object_or_404(Quiz, slug=slug)
    quiz_note =QuizNote(user=user, quiz=quiz)
    return render(
        request, 
        'dashboard/quiz_note.html',
        {
        'user': user,
        'quiz_note': quiz_note,
        'quiz': quiz
    })
