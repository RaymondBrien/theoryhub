from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from .models import Quiz, Question, Answer


class QuizList(generic.ListView):
    """
    Displays a list of all quizzes in :model:`quiz.Quiz`
    paginated by 6 quizzes per page.
    """
    queryset = Quiz.objects.all()
    template_name = 'quiz/quiz_list.html'
    paginate_by = 6

