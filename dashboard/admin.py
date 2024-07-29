from django.contrib import admin
from .models import UserQuizSubmission, QuizNote
@admin.register(UserQuizSubmission)
class UserQuizSubmissionAdmin(admin.ModelAdmin):
    list_display = ('owner', 'quiz', 'user_score', 'last_taken')
    
@admin.register(QuizNote)
class QuizNoteAdmin(admin.ModelAdmin): 
    list_display = ('user', 'note', 'created_at')