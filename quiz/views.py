from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
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
        All published instances of :model:`quiz.Quiz`.
    ``title``
            An instance of :model:`quiz.title`.
    ``questions``
            A queryset of :model:`quiz.Question` objects from quiz instance.
    
    **Template**
    :template:`quiz/single_quiz.html`
    """
    queryset = Quiz.objects.filter(status=1) 
    quiz = get_object_or_404(queryset, slug=slug)
    questions = Question.objects.filter(quiz=quiz)
    context = {
        'quiz': quiz,
        'questions': questions,
    }
    return render(request, 'quiz/single_quiz.html', context)


