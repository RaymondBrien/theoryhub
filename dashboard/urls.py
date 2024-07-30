from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  
    path('notes/', views.UserNote.as_view(), name='user_notes'),  
    path('notes/edit_note/<int:note_id>/', views.edit_note, name='edit_note'), #TODO debug
]