from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
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