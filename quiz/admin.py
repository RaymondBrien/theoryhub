from django.contrib import admin
from .models import Quiz
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Quiz)
class QuizAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('title', 'description', 'created_on', 'updated_on')
    list_filter = ('created_on', 'updated_on')
    search_fields = ('title', 'description')
    ordering = ('-created_on',)
    summernote_fields = ('description',)

# admin.site.register(Quiz)