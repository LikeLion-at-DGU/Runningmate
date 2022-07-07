from django.db import models
from django.contrib.auth.models import User


class Project(models.Model): #프로젝트 추가
    id = models.BigAutoField(help_text="Comment ID", primary_key=True) 
    startday = models.DateField(default='1000-01-01')
    endday = models.DateField(default='1000-01-01')
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=100)
    body = models.TextField(null=True)
    
    def startday(self):
        return self.startday
    
    def endday(self):
        return self.endday
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]



