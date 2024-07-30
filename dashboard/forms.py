from django import forms
from .models import QuizNote

class QuizNoteForm(forms.ModelForm):
    
    class Meta:
        model = QuizNote
        fields = ['note', ]
        widgets = {
            'note': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your note here'})
        } # TODO style here to make note smaller (or handle in local div in template)