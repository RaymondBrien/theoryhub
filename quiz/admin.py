from django.contrib import admin
from django import forms
from .models import Quiz, Question, Answer


class QuestionInline(admin.TabularInline):
    """
    Enables admin to assign questions to each quiz in single interface
    for ease of editing and quiz creation.
    
    **Context**
    :model: `quiz.Question`
    
    """
    model = Question

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    """
    Adds list of quizzes to admin page.
    
    **Context**
    :model: `quiz.Quiz`
    
    """
    list_display = ('title', 'status', 'created_on', 'updated_on')
    inlines = [QuestionInline]  # This will show a list of questions, not for editing

class AnswerInline(admin.TabularInline):
    """
    Enables admin to assign 4 multiple-choice answer options to each question in
    single interface for ease of editing and quiz creation.
    
    **Context**
    :model: `quiz.Answer`
    
    """
    model = Answer
    extra = 4
    max_num = 4

class QuestionAdminForm(forms.ModelForm):
    """
    Form to host interface for admin to create questions with assigned answers.
    Answers are connected via fk in question model and accessible with 
    AnswerInline class in QuestionAdmin class.
    
    Form validated to ensure at least one answer is correct.
    
    **Context**
    :model: `quiz.Question`
    """
    class Meta:
        model = Question
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Adds 4 multiple-choice answers to a single question admin page for easier
    quiz question generation.
    
    **Context**
    :form: `QuestionAdminForm`
    :inlines: `AnswerInline`
    
    """
    form = QuestionAdminForm
    inlines = [AnswerInline]
    list_display = ('points', 'quiz_id', 'question_text')
    # TODO: debug at least one answer correct validation
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        # Ensure at least one answer is correct for each question
        if not any(answer.correct == 1 for answer in form.instance.answers.exclude(pk=form.instance.pk)):
            form.add_error(None, "At least one answer must be marked as correct for each question.")

