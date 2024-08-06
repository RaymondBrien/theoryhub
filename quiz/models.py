from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))
CORRECT = ((0, "Incorrect"), (1, "Correct"))

POINTS = ((1, "Small"), (2, "Medium"))
QUESTION_NUMBER = ((1, ""), (2, ""))
ANSWER_OPTIONS = ((1, "A"), (2, "B"), (3, "C"), (4, "D"))


class Quiz(models.Model):
    """Stores a single quiz, which is a collection of questions"""

    title = models.CharField(max_length=200, unique=True, validators=[
        MinLengthValidator(5), MaxLengthValidator(20)])
    slug = models.SlugField(
        max_length=200, unique=True, default=slugify(title))
    description = models.TextField(validators=[
        MinLengthValidator(5), MaxLengthValidator(50)])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f'{self.title}'

    # slugify quiz title for url functionality
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]
        verbose_name_plural = "Quizzes"


class Question(models.Model):
    """Stores a single question related :model:`quiz.Quiz`"""

    quiz_id = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    question_image = CloudinaryField('image', default='placeholder')
    points = models.IntegerField(choices=POINTS, default=1)

    class Meta:
        ordering = ["question_text"]
        verbose_name_plural = "Questions"

    def __str__(self):
        return f'Question belongs to Quiz {self.quiz_id})'


class Answer(models.Model):
    """Stores a single answer related :model:`quiz.Question`"""

    question_id = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    answer_content = models.TextField(
        default='Put multiple-choice answer here')
    answer_option = models.IntegerField(choices=ANSWER_OPTIONS, null=False)
    correct = models.IntegerField(
        choices=CORRECT, default=0)  # default answer incorrect

    class Meta:
        ordering = ["answer_option"]
        verbose_name_plural = "Answers"
        # only one answer option per question (i.e. a, b, c, d only).
        # (a b, b, c) is invalid.
        unique_together = ("question_id", "answer_option")

    def __str__(self):
        return f'Answer: {self.answer_content}'
