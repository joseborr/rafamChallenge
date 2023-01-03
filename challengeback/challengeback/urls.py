"""challengeback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import frontPage, studentView, lessonView, studentFriendView,takeLessonView
from core.models import Student
from core.queries import *
from rest_framework import routers, serializers, viewsets

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Student
        fields = ['id','username','created_at']

class FriendshipSerializer(serializers.HyperlinkedModelSerializer):
    friends = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username'
    )
    class Meta:
        model = Friendship
        fields = ['friends','created_at']

class FriendsForSpecificUserSerializer(serializers.HyperlinkedModelSerializer):
    friends = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field ='username'
    )
    class Meta:
        model = Student
        fields = ['id','username','created_at','friends']

class MyLessonsSerializer(serializers.HyperlinkedModelSerializer):
    lessons = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field ='name'
    )
    class Meta:
        model = Lesson
        fields = ['name','lessons']

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

    

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'friendships',FriendshipViewSet)
router.register(r'myfriends/(?P<id>\d+)',MyFriendsViewSet, 'myfriends')
router.register(r'mylessons/(?P<id>\d+)', MyLessonsViewSet, 'mylessons')

urlpatterns = [
    path('api/',include(router.urls)),
    path('api/',include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', frontPage, name='frontpage'),#a partir de aca son url para vistas de prueba
    path('student/',studentView, name='student_reg'),
    path('lesson/', lessonView, name='lesson_reg'),
    path('<id>/friends/', studentFriendView, name='student_friends'),
    path('<id>/my_lessons/',takeLessonView, name='my_lessons'),
    
]
