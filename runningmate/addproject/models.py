from tabnanny import verbose
from django.db import models
from django.forms import *
from datetime import *

from django.contrib.auth.models import *


# Create your models here.
class Project(models.Model):
    startday = models.DateField('프로젝트 시작일', default = timezone.now) # 시작기간 입력 날짜만
    endday = models.DateField('프로젝트 마감일', default = timezone.now) # 종료기간 입력 날짜만
    title = models.CharField(max_length=20) # 과목명
    intro = models.CharField(max_length=50) # 프로젝트 상세내용
    

    class Meta: 
        verbose_name = '프로젝트'
        verbose_name_plural = '프로젝트들'
        