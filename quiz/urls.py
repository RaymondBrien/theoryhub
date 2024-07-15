from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Quizzes.as_view(), name='quiz-list'), # class based view 
    # path('<int:quiz-id>', views.single_quiz, name='single-quiz'), # function based view TODO: make view
]
