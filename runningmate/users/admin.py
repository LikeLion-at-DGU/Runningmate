from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "user",
    #    "phone",
    #    "mbti",
    #    "intro",
    )
    list_display_links = (
        "user",
    #    "phone",
    #    "mbti",
    #    "intro",
    )
    search_fields = (
        "user",
    #    "phone",
    #    "mbti",
    #    "intro",
    )