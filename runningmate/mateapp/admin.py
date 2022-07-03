from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "writer",
        "datetime",
        "body",
        "place",
    )
    list_display_links = (
        "id",
        "title",
        "writer",
        "datetime",
        "body",
        "place",
    )
    search_fields = (
        "id",
        "title",
        "writer",
        "datetime",
        "body",
        "place",
    )

