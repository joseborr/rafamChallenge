from django import forms
from core.models import Lesson

class LessonForm(forms.Form):
    name = forms.CharField(required=True, max_length=50)

class StudentForm(forms.Form):
    username = forms.CharField(required=True, max_length=50)