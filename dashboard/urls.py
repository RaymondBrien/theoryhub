from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:username>/', views.dashboard, name='user_dashboard'),  
]