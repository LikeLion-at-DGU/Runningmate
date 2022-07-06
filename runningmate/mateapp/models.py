from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField

# Create your models here.

class Calendar(models.Model): # 대시보드 캘린더 모델
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    place = models.CharField(max_length=20)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]
    
    class Meta:
        verbose_name = "캘린더"
        verbose_name_plural = "캘린더(들)"
# 캘린더 모델을 다룰거다라는 request를 보냄 but 반영이 안돼서 에러가뜸
# no such column 은 migrations 오류임

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()

class TodoTitle(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

    # def __str__(self):
    #     return self.title

    # def todotitle(self):
    #     return self.title

class TodoComment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(TodoTitle ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.post
    
    # def todocomment(self):
    #     return self.post