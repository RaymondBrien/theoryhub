from django.shortcuts import render
from .models import UserQuizSubmission


def dashboard(request):
    submissions = UserQuizSubmission.objects.filter(owner=request.user)
    return render(request, 'dashboard.html', {'submissions': submissions})
