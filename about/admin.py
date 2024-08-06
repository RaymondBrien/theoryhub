from django.contrib import admin
from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    Adds title and content for welcome page for admin to edit as needed

    **Context**
    :model: `about.About`
    :fields: ('title', 'content')

    **Template**
    :template: `about/about_list.html`

    """
    list_display = ('title', 'content')
