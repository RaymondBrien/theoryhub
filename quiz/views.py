from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic
from django.contrib.auth.models import User

from .models import Quiz, Question, Answer
from .forms import AnswerSelection
from dashboard.models import UserQuizSubmission


class QuizList(generic.ListView):
    """
    Displays a list of all published quizzes, paginated by 6 quizzes per page.

    **Context**
    :model: `quiz.Quiz`

    **Template**
    :template_name:`quiz/quiz_list.html`
    """
    queryset = Quiz.objects.filter(status=1)
    template_name = 'quiz/quiz_list.html'
    paginate_by = 6
    context_object_name = 'quiz_list'


@login_required
def single_quiz(request, slug):
    """
    Displays a single quiz with associated questions to authenticated user.
    Users post request (answer submission) handled with AnswerSelect form.

    Answers handled together with question instances to avoid multiple queries.
    Answer stored as UserQuizSubmission instance.

    **Context**
    :model: `quiz.Quiz`
    :model: `quiz.Question`
    :model: `quiz.Answer`
    :model: `dashboard.AnswerSelection`
    :model: `dashboard.UserQuizSubmission`
    :form: `quiz.AnswerSelection`

    **Template**
    :template:`quiz/single_quiz.html`

    """

    user = get_object_or_404(User, username=request.user)
    if not user.is_authenticated:
        messages.info(
            request, "Access denied. Please log in to view this page.")
        return redirect(reverse('login'))

    queryset = Quiz.objects.filter(status=1)
    quiz = get_object_or_404(queryset, slug=slug)
    questions = Question.objects.filter(quiz_id=quiz)

    if request.method == "POST":
        # render quiz-specific fields with form
        answer_form = AnswerSelection(data=request.POST, quiz=quiz)

        if answer_form.is_valid():
            score = 0
            for question in quiz.questions.all():
                answer_id = answer_form.cleaned_data[f'question_{question.id}']
                answer = Answer.objects.get(id=answer_id)
                if answer.correct:
                    score += question.points

            UserQuizSubmission.objects.create(
                owner=user,
                quiz=quiz,
                user_score=score,
            )
            messages.success(
                request,
                f'Thank you {request.user.username}, your quiz is submitted successfully.')  # noqa
            return redirect('quiz_result', slug=quiz.slug)

    else:
        # dynamically generate form fields in get request
        answer_form = AnswerSelection(quiz=quiz)

    context = {
        'quiz': quiz,
        'questions': questions,
        'answer_form': answer_form,
    }

    return render(request, 'quiz/single_quiz.html', context)


@login_required
def quiz_result(request, slug):
    """
    Displays the result of latest user's quiz submission.
    Only visible immediately after quiz submission.

    Helper function to calculate maximum points avialable per quiz.

    **Context**
    :model: `quiz.Quiz`
    :model: `dashboard.UserQuizSubmission`

    **Template**
    :template_name:`quiz/quiz_result.html`

    """

    quiz = get_object_or_404(Quiz, slug=slug)
    submission = UserQuizSubmission.objects.filter(
        owner=request.user, quiz=quiz).order_by('-last_taken').first()

    def calculate_total_possible_score(quiz):
        max_score = sum([question.points for question in quiz.questions.all()])
        return max_score

    context = {
        'quiz': quiz,
        'submission': submission,
        'max_score': calculate_total_possible_score(quiz)
    }

    return render(request, 'quiz/quiz_result.html', context)
