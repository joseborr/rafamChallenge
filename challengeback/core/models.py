from django.db import models
from datetime import datetime


class Student(models.Model):
    username = models.CharField(unique=True,max_length=50)
    created_at = models.DateTimeField(editable=False, null=True)
    updated_at = models.DateTimeField(null=True)
    

    def save(self,*args,**kwargs):
        ''' On save, update timestamps '''
        if not self.id :
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return super(Student,self).save(*args,**kwargs)

    def __str__(self):
        return self.username
    
class Lesson(models.Model):
    name = models.CharField(unique=True,max_length=50)
    students = models.ManyToManyField(Student,blank=True)
    created_at = models.DateTimeField(editable=False, null=True)
    updated_at = models.DateTimeField(null=True)

    def save(self,*args,**kwargs):
        ''' On save, update timestamps '''
        if not self.id :
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return super(Lesson,self).save(*args,**kwargs)

    def __str__(self):
        return self.name


class Friendship(models.Model):
    friends = models.ManyToManyField(Student,blank=True)
    created_at = models.DateTimeField(editable=False, null=True)
    updated_at = models.DateTimeField(null=True)

    def save(self,*args,**kwargs):
        ''' On save, update timestamps '''
        if not self.id :
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return super(Friendship,self).save(*args,**kwargs)
    
