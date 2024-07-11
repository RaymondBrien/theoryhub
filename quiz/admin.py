from django.contrib import admin
from .models import Quiz, Question, Answer

class QuestionInline(admin.TabularInline):
    model = Question

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    """Adds question list to quiz admin page"""
    list_display = ('title', 'status', 'created_on', 'updated_on' )
    # inlines = [QuestionInline,] # TODO: don't edit questions here, just have list of questions.
    
    
class AnswerInline(admin.TabularInline):
    """Each question has 4 answer options (multiple choice)"""
    model = Answer
    # extra = 4 # TODO: bug, if go to edit, adds another 4 blank answers to complete. 


class QuestionAdmin(admin.ModelAdmin):
    """Adds 4 multiple-choice answers to a single question admin page."""
    model = Question
    inlines = [AnswerInline,]
    list_display = ( 'points', 'quiz_id', 'question_text')
    

admin.site.register(Question, QuestionAdmin) # single question admin page with 4 answer options