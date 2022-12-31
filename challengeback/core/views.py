from django.shortcuts import render,redirect
from core.forms import StudentForm, LessonForm
from core.models import Student,Lesson,Friendship
from core.queries import *


def frontPage(request):
    courses = list_all_lessons()
    context = {'lessons':courses}
    return render(request,'frontPage.html',context)

def studentView(request):
    if request.method == 'POST' :
        form = StudentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            student = Student()
            student.username = username
            student.save()

            return redirect(frontPage)
    else:
        form = StudentForm()
    context = {'form':form }
    return render(request,'student_reg.html', context)

def lessonView(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lesson = Lesson()
            lesson.name = name
            lesson.save()

            return redirect(frontPage)
    else:
        form = LessonForm()
    context = {'form':form}
    return render(request,'lesson_reg.html',context)
