from django.contrib import admin

from addproject.models import *
from .models import *

# Register your models here.
# admin.site.register(Todo)
admin.site.register(Post)


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
