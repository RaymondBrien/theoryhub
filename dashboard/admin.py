from django.contrib import admin
from .models import UserQuizSubmission, QuizNote


@admin.register(UserQuizSubmission)
class UserQuizSubmissionAdmin(admin.ModelAdmin):
    """
    Send User Quiz Submission results to the admin for monitoring.

    **Context**
    :model: `dashboard.UserQuizSubmission`

    """
    list_display = ('owner', 'quiz', 'user_score', 'last_taken')


@admin.register(QuizNote)
class QuizNoteAdmin(admin.ModelAdmin):
    """
    Send QuizNote instances to the admin for monitoring.

    **Context**
    :model: `dashboard.QuizNote`

    """
    list_display = ('user', 'note', 'created_at')
