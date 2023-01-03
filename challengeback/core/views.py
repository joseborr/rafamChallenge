from django.shortcuts import render,redirect
from rest_framework import viewsets

from core.forms import StudentForm, LessonForm, FriendshipForm, TakeLessonForm
from core.models import Student,Lesson,Friendship
from core.queries import *
from core.serializers import MyLessonsSerializer, StudentSerializer, FriendshipSerializer, FriendsForSpecificUserSerializer

class MyLessonsViewSet(viewsets.ModelViewSet):
    serializer_class = MyLessonsSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        student = get_student_by_id(id)
        return list_lessons_from_student(student)


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = list_all_students()
        

class FriendshipViewSet(viewsets.ModelViewSet):
    serializer_class = FriendshipSerializer
    queryset = list_all_friendships()
 

class MyFriendsViewSet(viewsets.ModelViewSet):
    serializer_class = FriendsForSpecificUserSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        return list_student_friends(id)


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
            accept_friendship(me,friend) 
    else:
        form = FriendshipForm()

    context = {'friends':friends, 'form':form, 'me':me}
    return render(request,'student_friends.html',context)

def takeLessonView(request,id):
    me = get_student_by_id(id)
    my_lessons = list_lessons_from_student(me)
    my_lessons = my_lessons if my_lessons else ('No lessons yet',)
    if request.method == 'POST':
        form = TakeLessonForm(request.POST)
        if form.is_valid():
            lesson = form.cleaned_data['lessons']
            sign_up_course(me,lesson)
    else:
        form = TakeLessonForm()
    context = {'form':form, 'lessons':my_lessons,'me':me}
    return render(request,'take_lessons.html',context)
            