from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Calendar(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()