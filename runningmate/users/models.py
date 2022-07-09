from distutils.command.upload import upload
from operator import mod
from textwrap import indent
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField

# 모델 수정 및 생성시 makemigrations > migrate 꼭 필요
# DB는 그냥 table 인데 DB 건드릴 때, makemigrations 해야함 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 유저 삭제시 프로필도 같이 삭제됨
    last_name = models.CharField(max_length=10, default="")
    first_name = models.CharField(max_length=10, default="")
    phone = models.CharField(max_length=13) # 폰 번호
    timetable = models.ImageField(upload_to = "calendar/", blank=True, null=True) # 사용자들이 시간표를 올릴 때마다 media/calendar에 저장됨
    profile = models.ImageField(blank=True, null=True)
    major = models.CharField(max_length=20, null=True) # 학과

    class Meta:
        verbose_name = "프로필"
        verbose_name_plural = "프로필(들)"

        ## 프로필 사항 추가 및 변경