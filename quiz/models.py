from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
CORRECT = ((0, "Incorrect"), (1, "Correct" ))

POINTS= ((1, "Small"), (2, "Medium" ))
QUESTION_NUMBER = ((1, ""), (2, ""))
ANSWER_OPTIONS = ((1, "A"), (2, "B"), (3, "C"), (4, "D"))

class Quiz(models.Model):
    """Stores a single quiz, which is a collection of questions"""

    title = models.CharField(max_length=200, unique=True, validators=[MinLengthValidator(5), MaxLengthValidator(20)])
    description = models.TextField(validators=[MinLengthValidator(5), MaxLengthValidator(50)])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default =0)

# TODO Date field validation for published vs draft quiz - copy to questions too
# https://docs.djangoproject.com/en/4.2/ref/models/instances/#django.db.models.Model.clean_field
    # def clean(self):
    # # Don't allow draft entries to have a pub_date.
    # if self.status == "draft" and self.pub_date is not None:
    #     raise ValidationError(_("Draft entries may not have a publication date."))
    # # Set the pub_date for published items if it hasn't been set already.
    # if self.status == "published" and self.pub_date is None:
    #     self.pub_date = datetime.date.today()
    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "Quizzes"
    def __str__(self):
        return f'{self.title}'


class Question(models.Model):
    """Stores a single question related :model:`quiz.Quiz`"""
    # TODO: check how many types of point questions there are, and update integer choices accordingly. 
    # TODO: make question numbers - how many per quiz?
    
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    question_image = CloudinaryField('image', default='placeholder')
    points = models.IntegerField(choices=POINTS, default=1)
        
    class Meta:
        ordering = ["question_text"]
        verbose_name_plural = "Questions"
    def __str__(self):
        return f'Question: {self.question_text} (belongs to Quiz {self.quiz_id})'
        
        #     QUESTIONS = {
        #     0: "",
        #     1: "What is your name?",
        #     2: "How old are you?",
        #     # ... more questions ...
        # }
        # from django.utils.translation import gettext_lazy as _

        # class QuestionNumber(models.TextChoices):
        #     EMPTY = '', _('')
        #     QUESTION_1 = '1', _('What is your name?')
        #     QUESTION_2 = '2', _('How old are you?')
        #     # ... more questions ...

        #     question_number = models.IntegerField(choices=[(k, v) for k, v in QUESTIONS.items()])
    



class Answer(models.Model):
    """Stores a single answer related :model:`quiz.Question`"""
    
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_content = models.TextField(default='Put multiple-choice answer here',)
    answer_option = models.IntegerField(choices=ANSWER_OPTIONS, default=1)
    # TODO: how do I make sure there is always ONE correct answer per question?
    correct = models.IntegerField(choices=CORRECT, default=0) # additional field added after ERD
    
    class Meta:
        ordering = ["answer_option"]
        verbose_name_plural = "Answers"
        unique_together = ("question_id", "answer_option") # only one answer per answer option per question