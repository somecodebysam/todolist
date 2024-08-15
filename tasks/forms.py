from django import forms
from .models import Task
from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_future_datetime(value):
    if value and value <= timezone.now():
        raise ValidationError('Please enter a future date and time.')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date']

        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['due_date'].required = False

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        validate_future_datetime(due_date)
        return due_date