from django.db import models
from django.contrib.auth.models import User
from quiz.models import Quiz


# Create your models here.
#  who owns 
#  date 
#  content 
#  what quiz (imported quiz model) fk to quiz id 

 
class UserQuizSubmission(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='user_quiz_score')
    user_score = models.IntegerField(null=True, default=0)  # empty if no quiz taken yet
    last_taken = models.DateField(auto_now_add=True)
 