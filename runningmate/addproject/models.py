from django.db import models
from django.contrib.auth.models import User


class Project(models.Model): #프로젝트 추가
    id = models.BigAutoField(help_text="Comment ID", primary_key=True) 
    startday = models.DateField()
    endday = models.DateField()
    title = models.CharField(max_length=200)
    body = models.TextField(null=True)

    def __str__(self):
        return self.startday
    
    def __str__(self):
        return self.endday
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]

        ## test ## 