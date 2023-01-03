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

from rest_framework import routers

from core.views import frontPage, studentView, lessonView, studentFriendView,takeLessonView
from core.views import StudentViewSet, FriendshipViewSet, MyFriendsViewSet, MyLessonsViewSet
   

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
