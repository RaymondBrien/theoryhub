from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Quiz, Question, Answer


class Quizzes(generic.ListView):
    """
    Displays a list of all quizzes in :model:`quiz.Quizzes`
    paginated by 6 quizzes per page.
    """
    queryset = Quiz.objects.filter(status=1) #  only display published quizzes
    template_name = 'quiz/quiz_list.html'
    paginate_by = 6
    context_object_name = 'quizzes'



