from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(Todo)
admin.site.register(Post)

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "writer",
        "startday",
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
        "startday",
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
        "startday",
        "endday",
        "starttime",
        "endtime",
        "body",
        "place",
    )
