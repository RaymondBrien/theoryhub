from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
class Quiz(models.Model):
    """Stores a single quiz, which is a collection of questions"""

    title = models.CharField(max_length=200, unique=True, validators=[MinLengthValidator(5), MaxLengthValidator(20)] )
    description = models.TextField(validators=[MinLengthValidator(5), MaxLengthValidator(50)] )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default =0)

# TODO add messages if not valid field before try to save?
# TODO Date field validation for published vs draft quiz - copy to questions too
# https://docs.djangoproject.com/en/4.2/ref/models/instances/#django.db.models.Model.clean_fields
    # STATUS_CHOICES = (
    #     ('draft', 'Draft'),
    #     ('published', 'Published'),
    # )
    # def clean(self):
    # # Don't allow draft entries to have a pub_date.
    # if self.status == "draft" and self.pub_date is not None:
    #     raise ValidationError(_("Draft entries may not have a publication date."))
    # # Set the pub_date for published items if it hasn't been set already.
    # if self.status == "published" and self.pub_date is None:
    #     self.pub_date = datetime.date.today()
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