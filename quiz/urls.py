from django.urls import path, include
from . import views

urlpatterns = [
    path('quiz_list/', views.QuizList.as_view(), name='quiz_list'), # class based view 
    path('quiz/<str:title>/', views.single_quiz, name='single_quiz'), # function based view TODO: make view
]
