from django.db import models
from django.contrib.auth.models import User
from quiz.models import Quiz

class UserQuizSubmission(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='user_quiz_score')
    user_score = models.IntegerField(null=True, default=0)  # empty if no quiz taken yet
    last_taken = models.DateField(auto_now_add=True)
 