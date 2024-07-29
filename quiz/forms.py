from django import forms
from .models import QuizNote

# collect user answers for each question in quiz submission
# fields dynamically generated based on questions, not tied to specific model

class AnswerSelection(forms.Form): # custom form not for specific model for more flexibility
    def __init__(self, *args, **kwargs): # accept any number of positional and keyword arguments
        quiz = kwargs.pop('quiz') # use quiz object to generate form fields
        super(AnswerSelection, self).__init__(*args, **kwargs) # constructor for parent class: ensure standard args are handled properly and form is correctly initialised
        for question in quiz.questions.all():
            self.fields[f'question_{question.id}'] = forms.ChoiceField( # for each question, create new form field
                choices=[(answer.id, answer.answer_content) for answer in question.answers.all()], # tuple: (value, label) -> (id, content)
                widget=forms.RadioSelect,
                required=True,
                label=question.question_text
            ) # TODO add back the image for each question!!


class QuizNoteForm(forms.ModelForm):
    class Meta:
        model = QuizNote
        fields = ['note', ]
        widgets = {
            'note': forms.Textarea(attrs={'class': 'form-control, height: 1em', 'placeholder': 'Enter your note here'})
        } # TODO style here to make note smaller (or handle in local div in template)