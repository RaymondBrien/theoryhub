from django.urls import path, include
from . import views

urlpatterns = [
    path('quiz_list/', views.QuizList.as_view(), name='quiz_list'), # class based view
    path('<slug:slug>/', views.single_quiz, name='single_quiz'), # function based view
]
