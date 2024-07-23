from django import forms
from .models import Answer

class AnswerSelection(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer_option',)
