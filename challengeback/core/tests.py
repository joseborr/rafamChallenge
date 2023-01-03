from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


from core.models import Student
from core.queries import *

class StudentTest(APITestCase):
    fixtures = ['lessons.json','students.json']

    def setUp(self):
        self.joe = get_student_by_id(1)
        self.mark = get_student_by_id(2)
        self.jodie = get_student_by_id(3)
        self.rachel = get_student_by_id(4)
        self.sara = get_student_by_id(5)

    def test_friendships_api(self):
        '''test all the friendships data, and size'''

        response = self.client.get('/api/friendships/')
        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

        accept_friendship(self.joe,self.mark)
        response = self.client.get('/api/friendships/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        created = response.data[0]['created_at']
        self.assertEqual(response.data,[{"friends": ["Joe","Mark"],"created_at": created}])


    def test_myfriends_api(self):
        '''test friendship of student with id = 1'''

        response = self.client.get('/api/myfriends/1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
        accept_friendship(self.joe,self.mark)
        accept_friendship(self.joe,self.jodie)
        accept_friendship(self.joe,self.rachel)

        response = self.client.get('/api/myfriends/1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_users_api(self):
        '''test all the students data and size'''

        response = self.client.get('/api/students/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        student = response.data[0]
        created = response.data[0]["created_at"]
        self.assertEqual(student,{"id": 3,"username": "Jodie","created_at": created})

    def test_mylessons_api(self):
        '''test lessons of student with id = 1'''

        response = self.client.get('/api/mylessons/1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),0)
        lesson = get_lesson_by_id(2)
        sign_up_course(self.joe, lesson)
        response = self.client.get('/api/mylessons/1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,[{"name": "Algebra","topic": "Matemática"}])
    

        
        
        


