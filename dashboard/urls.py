from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  
    path('notes/', views.UserNote.as_view(), name='user_notes'),  
    path('notes/new_note', views.user_note, name='new_note'),  
]