from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin): # 장고 기본 모델이름과 충돌 될까봐 변경
    list_display = (
        "user",
        "phone",
        "major",
        "timetable",
        "profile",
        
    )
    list_display_links = (
        "user",
        "phone",
<<<<<<< HEAD
        "timetable",
        "profile",
=======
        "major",
        "timetable",
>>>>>>> ee3364b74d071713bdbf527909454d7af50cf00f
    )
    search_fields = (
        "user",
        "phone",
        "major",
        "timetable",
        "profile",
    )