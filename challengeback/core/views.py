from django.shortcuts import render,redirect
from core.forms import StudentForm, LessonForm, FriendshipForm
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
    students = list_all_students()
    context = {'form':form, 'students':students }
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

def studentFriendView(request, id):
    me = get_student_by_id(id)
    friends =  list_student_friends(id)
    friends = friends if friends else ('No friends yet',)
    if request.method == 'POST':
        form = FriendshipForm(request.POST)
        if form.is_valid():
            friend = form.cleaned_data['students']
            student = get_student_by_id(id)
            accept_friendship(student,friend) 
    else:
        form = FriendshipForm()

    context = {'friends':friends, 'form':form, 'me':me}
    return render(request,'student_friends.html',context)

 