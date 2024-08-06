from django import forms
from .models import QuizNote


class QuizNoteForm(forms.ModelForm):
    """
    Form for quiz note instance used in dashboard notes page.

    **Context**
    :model: `dashboard.Quiznote`
    :fields: ('note')

    **Template**
    :template: `dashboard/notes_page.html`

    """
    class Meta:
        model = QuizNote
        fields = ['note', ]
        widgets = {
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your note here'
                })
        }
