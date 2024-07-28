from django.contrib import admin
from django import forms
from .models import Quiz, Question, Answer, QuizNote

class QuestionInline(admin.TabularInline):
    model = Question
    # TODO: do I need show_change_link?
    # show_change_link = True  # This allows editing questions from the quiz page

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    """Adds question list to quiz admin page"""
    list_display = ('title', 'status', 'created_on', 'updated_on')
    inlines = [QuestionInline]  # This will show a list of questions, not for editing

class AnswerInline(admin.TabularInline):
    """Each question has 4 answer options (multiple choice)"""
    model = Answer
    extra = 4
    max_num = 4

class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

    def clean(self):
        # TODO debug 
        cleaned_data = super().clean()
        # answers = self.instance.answers.all() # if self.instance.pk else []
        
        # if not any(answer.correct == 1 for answer in answers):
        #     raise forms.ValidationError("At least one answer must be marked as correct.")
        # return cleaned_data

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Adds 4 multiple-choice answers to a single question admin page."""
    form = QuestionAdminForm
    inlines = [AnswerInline]
    list_display = ('points', 'quiz_id', 'question_text')
    # TODO: debug at least one answer correct validation
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        # Ensure at least one answer is correct for each question
        if not any(answer.correct == 1 for answer in form.instance.answers.exclude(pk=form.instance.pk)):
            form.add_error(None, "At least one answer must be marked as correct for each question.")
            # form.instance.delete()

    # validate using forms for easier validation
    # def save_formset(self, request, form, formset, change):
    #     instances = formset.save(commit=False)
    #     for instance in instances:
    #         instance.save()
    #     formset.save_m2m()
        
        # # Check if at least one answer is correct after saving
        # if not any(answer.correct == 1 for answer in form.instance.answers.all()):
        #     form.add_error(None, "At least one answer must be marked as correct.")
        #     return
        
        # formset.save()


# admin.site.register(Answer)  # If you want to manage answers separately

@admin.register(QuizNote)
class QuizNoteAdmin(admin.ModelAdmin): 
    list_display = ('user', 'quiz', 'note', 'created_at')