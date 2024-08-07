from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from quiz.models import Quiz


class UserQuizSubmission(models.Model):
    """
    Represents a user's submission time and score
    for a quiz related to :model:`auth.User` and :model:`quiz.Quiz`

    Note: user can take quiz more than once.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='user_quiz_score')
    # user_score empty if no quiz taken yet
    user_score = models.IntegerField(null=True, default=0)
    last_taken = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-last_taken']

    def __str__(self):
        return f'{self.owner.username} | Score: {
            self.user_score} on quiz: {self.quiz.title} at: {self.last_taken}'


class QuizNote(models.Model):
    """
    Stores single note related to :model:`quiz.Quiz` and :model:`auth.User`
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if len(self.note) < 10:
            raise ValidationError('Note must be at least 10 characters long')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'QuizNote added by {self.user.username}'
