from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from cloudinary.models import CloudinaryField


class Quiz(models.Model):
    """Stores a single quiz, which is a collection of questions"""

    title = models.CharField(max_length=200, unique=True, validators=[MinLengthValidator(5), MaxLengthValidator(10)] )
    description = models.TextField(validators=[MinLengthValidator(5), MaxLengthValidator(50)] )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder') 

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = 'Quizzes'
    def __str__(self):
        return f'Title: {self.title}'


class Question(models.Model):
    """Stores a single question related :model:`quiz.Quiz`"""

    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')

    # TODO: check how to best format question text so it's multiple choice, see django docs
    # TODO: question_options class? Or pulled from answers, with correct/incorrect bool on answers model? # changed from ERD question_text as each question is multiple choice 
    question_text = models.TextField()
    
    # TODO: check how many types of point questions there are, and update integer choices accordingly. 
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/
    class Points(models.IntegerChoices):
        SMALL = 1
        MEDIUM = 2
        BIG = 3

    points = models.IntegerField(choices=Points.choices)

    # class Meta:


class Answer(models.Model):
    """Stores a single answer related :model:`quiz.Question`"""
    
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_num = models.IntegerField()
    correct = models.BooleanField() # additional field added after ERD