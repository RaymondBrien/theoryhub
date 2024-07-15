from django.urls import path, include
from . import views

urlpatterns = [
    path('quiz_list/', views.QuizList.as_view(), name='quiz_list'), # class based view 
    # path('<int:quiz-id>', views.single_quiz, name='single-quiz'), # function based view TODO: make view
]
