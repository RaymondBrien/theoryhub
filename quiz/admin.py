from django.contrib import admin
from .models import Quiz, Question, Answer
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)


# @admin.register(Quiz)
# class QuizAdmin(SummernoteModelAdmin):
#     """
#     Admin for Quiz creation interface: 
#     create single instance of Quiz.
#     """
#     list_display = ('title', 'description', 'created_on', 'updated_on')
#     list_filter = ('created_on', 'updated_on')
#     search_fields = ('title', 'description')
#     ordering = ('-created_on',)
#     summernote_fields = ('description',)
