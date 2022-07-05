from django.db import models
from django.contrib.auth.models import User


class Project(models.Model): #프로젝트 추가
    startday = models.DateField('프로젝트 시작일')
    endday = models.DateField('프로젝트 마감일')
    title = models.CharField(max_length=200)
    intro = models.CharField(max_length=100)


    
    class Meta:
        verbose_name = "프로젝트"
        verbose_name_plural = "프로젝트"