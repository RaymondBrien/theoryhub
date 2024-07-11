from django.contrib import admin
from .models import Quiz, Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4 # each question is multiple choice, with 4 options

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [AnswerInline,] 
    

# This currently won't work. (Quiz -> Question -> Answers)
# To work around this limitation, you would typically 
# manage Answer objects directly within the Question admin page without using nested inlines. 
# Alternatively, you can look into third-party packages that extend Django's admin to 
# support nested inlines or implement custom views or forms that manually handle the nesting logic.


admin.site.register(Question, QuestionAdmin)