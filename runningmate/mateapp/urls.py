from django.urls import path
from .views import *


app_name = "mateapp"
urlpatterns = [
    path('mainpage',showmain, name = "showmain"),
    path('calendar',calendar, name = "calendar"),
    path('showevent',showevent, name = "showevent"),
    path('', login, name="login"),
    path('timetable',timetable, name='timetable'),
    path('todolist', todolist, name="todolist"),
    path('todocreate/', todocreate, name='todocreate'),
    path('todoupdate/<str:pk>/', todoupdate, name='todoupdate'),
    path('tododelete/<str:pk>/', tododelete, name='tododelete'),
]