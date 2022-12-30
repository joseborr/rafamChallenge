from django.db import models


class Student(models.Model):
    username = models.CharField(unique=True,max_length=50)
    created_at = models.DateTimeField
    
class Courses(models.Model):
    name = models.CharField(unique=True,max_length=50)
    created_at = models.DateTimeField

class Friendship(models.Model):
    students = models.ManyToManyField(Student,blank=True)
    created_at = models.DateTimeField
