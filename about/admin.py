from django.contrib import admin
from .models import About

@admin.register(About)
class AboutAdmin(admin. ModelAdmin):
    """
    Adds about title and content for about 
    page for admin to edit as needed
    """
    list_display = ('title', 'content', )