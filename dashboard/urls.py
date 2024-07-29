from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  
    path('quiz_notes/', views.quiz_note, name='quiz_notes'),  
]