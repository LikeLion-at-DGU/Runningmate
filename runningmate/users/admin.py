from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): # 장고 기본 모델이름과 충돌 될까봐 변경
    list_display = (
        "user",
        "phone",
        "timetable",
        
    )
    list_display_links = (
        "user",
        "phone",
         "timetable",
    )
    search_fields = (
        "user",
        "phone",
        "timetable",
    )