from django.db import models
from django.contrib.auth.models import User


class Project(models.Model): #프로젝트 추가
<<<<<<< HEAD
    id = models.BigAutoField(help_text="Comment ID", primary_key=True) # 
    startday = models.DateField()
    endday = models.DateField()
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=100)
    body = models.TextField(null=True)

    def startday(self):
        return self.startday
    
    def endday(self):
        return self.endday
    
    def title(self):
=======
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
>>>>>>> ab65593bae3cb97030c9ff423593f746cae9c5d9
        return self.title
    
    def summary(self):
        return self.body[:30]
<<<<<<< HEAD
=======

        ## test ## 
>>>>>>> ab65593bae3cb97030c9ff423593f746cae9c5d9
