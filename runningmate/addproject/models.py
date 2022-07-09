from ast import MatchSequence
from csv import writer
from operator import mod
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField

class Project(models.Model): #프로젝트 추가
    id = models.AutoField(help_text="Comment ID", primary_key=True) 
    startday = models.DateField(default='1000-01-01')
    endday = models.DateField(default='1000-01-01')
    title = models.CharField(max_length=200)
    body = models.TextField(null=True)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='following')

    def __str__(self):
        return self.startday
    
    def __str__(self):
        return self.endday
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]
    
    COLOR_CHOICES = [
        ("#50cfbc","1",),("#fe7782","2",),("#45bfff","3",),("#ffbc54","4",),("#735bf2","5",),
        ]
    color = ColorField(choices=COLOR_CHOICES)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)



