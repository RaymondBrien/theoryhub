from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  
    path('notes/', views.user_notes, name='user_notes'),  
    path('notes/edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    path('notes/delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    
    
]