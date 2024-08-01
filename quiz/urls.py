from django.urls import path, include
from . import views

urlpatterns = [
    path('quiz_list/', views.QuizList.as_view(), name='quiz_list'),
    path('<slug:slug>/', views.single_quiz, name='single_quiz'),
    path('<slug:slug>/quiz_result/', views.quiz_result, name='quiz_result'),
]
