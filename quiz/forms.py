from django import forms


class AnswerSelection(forms.Form):
    """
    Custom form not for specific model for more flexibility.
    Collects user answers for each question in quiz submission

    Fields are dynamically generated based on questions,
    not tied to specific model for future scalability.

    **Context**
    :model: `quiz.Quiz`

    """
    def __init__(self, *args, **kwargs):
        # use quiz object here to generate form fields
        quiz = kwargs.pop('quiz')
        # initialize form according to quiz object
        super(AnswerSelection, self).__init__(*args, **kwargs)

        for question in quiz.questions.all():
            # for each question, create new form field
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=[(
                    answer.id, answer.answer_content) for answer in question.answers.all()],  # noqa
                # tuple: (value, label) -> (id, content),
                widget=forms.RadioSelect,
                required=True,
                label=question.question_text,
        )
