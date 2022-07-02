from django.contrib import admin
from .models import *
from .models import Todo

# Register your models here.

admin.site.register(Todo)

@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "writer",
        "datetime",
        "body",
    )
    list_display_links = (
        "id",
        "title",
        "writer",
        "datetime",
        "body",
    )
    search_fields = (
        "id",
        "title",
        "writer",
        "datetime",
        "body",
    )
