from django.contrib import admin

from addproject.models import *
from .models import *

# Register your models here.
# admin.site.register(Todo)
admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "day",
    )
    list_display_links = (
        "title",
        "user",
        "day",
    )
    search_fields = (
        "title",
        "user",
        "day",
    )

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "writer",
        "endday",
        "starttime",
        "endtime",
        "body",
        "place",
    )
    list_display_links = (
        "id",
        "title",
        "writer",
        "endday",
        "starttime",
        "endtime",
        "body",
        "place",
    )
    search_fields = (
        "id",
        "title",
        "writer",
        "endday",
        "starttime",
        "endtime",
        "body",
        "place",
    )
