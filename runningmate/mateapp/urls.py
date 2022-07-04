from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers

app_name = "mateapp"
urlpatterns = [
    path('mainpage',showmain, name = "showmain"),
    path('calendar',calendar, name = "calendar"),
    path('', login, name="login"),
    path('timetable',timetable, name='timetable'),
    path('todo_new/', todo_new, name="todo_new")
]
