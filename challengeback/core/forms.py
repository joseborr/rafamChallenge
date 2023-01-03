from django import forms
from core.models import Lesson
from core.queries import list_all_students, list_all_lessons

class LessonForm(forms.Form):
    name = forms.CharField(required=True, max_length=50)


class StudentForm(forms.Form):
    username = forms.CharField(required=True, max_length=50)

class FriendshipForm(forms.Form):
    friends = (list_all_students())
    students = forms.ModelChoiceField( queryset=friends ,label='Students to be friend')

class TakeLessonForm(forms.Form):
    courses = list_all_lessons()
    lessons = forms.ModelChoiceField(queryset=courses, label='Lessons to take')