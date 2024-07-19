from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.db.models import Prefetch
from django.contrib.auth.models import User

from .models import Quiz, Question, Answer


class QuizList(generic.ListView):
    """
    Displays a list of all quizzes in :model:`quiz.Quizzes`
    paginated by 6 quizzes per page.
    """
    queryset = Quiz.objects.filter(status=1) #  only display published quizzes
    template_name = 'quiz/quiz_list.html'
    paginate_by = 6
    context_object_name = 'quiz_list'


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
    
    # Prefetch related answers to avoid multiple database queries
    # answers_prefetch = Prefetch('answers', queryset=Answer.objects.all())
    questions = Question.objects.filter(quiz_id=quiz)
    # .prefetch_related(answers_prefetch)

    context = {
        'quiz': quiz,
        'questions': questions,
    }
    return render(request, 'quiz/single_quiz.html', context)


# To fix this issue, you should aim to pass the answers related to each question 
# to the template in a way that they can be iterated over together. 
# One common approach is to modify the Question queryset to prefetch related Answer objects. 
# This way, you don't filter Answer objects separately but access them through their relation to 
# Question objects.

