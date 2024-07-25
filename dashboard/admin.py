from django.contrib import admin
from .models import UserQuizSubmission


@admin.register(UserQuizSubmission)
class UserQuizSubmissionAdmin(admin.ModelAdmin):
    list_display = ('owner', 'quiz', 'user_score', 'last_taken')