from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Post(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=200)
#     writer = models.ForeignKey(User,on_delete=models.CASCADE)
    # pub_date = models.DateTimeField()
    # body = models.TextField()
    # image = models.ImageField(upload_to = "post/", blank=True, null=True)

def __str__(self):
    return self.title

def summary(self):
    return self.body[:10]

class Post(models.Model):
    userName = models.CharField(max_length=20) # 이름 입력 최대 20글자
    userAbility = models.CharField(max_length=20) # 이름 입력 최대 20글자
    writer = models.ForeignKey(User,on_delete=models.CASCADE) # 작성자 누군지
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "post/", blank=True, null=True)
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]



class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post ,on_delete=models.CASCADE, related_name ='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
