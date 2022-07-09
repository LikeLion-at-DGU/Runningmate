from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): # 장고 기본 모델이름과 충돌 될까봐 변경
    list_display = (
        "user",
        "last_name",
        "first_name",
        "phone",
        "major",
        "timetable",
        "profile",
        
    )
    list_display_links = (
        "user",
        "last_name",
        "first_name",
        "phone",
        "major",
        "timetable",
        "profile",        
    )
    search_fields = (
        "user",
        "last_name",
        "first_name",
        "phone",
        "major",
        "timetable",
        "profile",
    )