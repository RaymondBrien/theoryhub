from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Quizzes.as_view(), name='home'), # class based view 
    # path('create-quiz/', views.CreateQuiz, name='create-quiz'),  # Add this path to create a new quiz instance
]
