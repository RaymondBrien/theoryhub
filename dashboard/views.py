from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from quiz.models import Quiz
from .models import UserQuizSubmission

def dashboard(request, username):
    """
    Context 
    Template
    
    """
    user = get_object_or_404(User, username=username)
    submissions = UserQuizSubmission.objects.filter(owner=user) 
    return render(request, 'dashboard/dashboard.html', {'submissions': submissions, 'user': user})