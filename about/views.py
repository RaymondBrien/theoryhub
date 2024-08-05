from django.shortcuts import render
from django.views import generic

from .models import About

def about(request):
    """
    Shows about page with all content
    """
    about_list = About.objects.first()
    template_name = 'about/about_list.html'
    context = {
        'about_list': about_list,
    }
    return render(request, template_name, context)