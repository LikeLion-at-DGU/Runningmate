from django.urls import path
from .views import *
app_name = "mateapp"
urlpatterns = [
    path('mainpage',showmain, name = "showmain"),
    path('calendar',calendar, name = "calendar"),
    path('', login, name="login"),
    path('timetable',timetable, name='timetable'),
    path('newproject/',newproject, name='newproject'),
    path('create_project/',create_project, name="create_project"),
    path('detail_project/',detail_project, name="detail_project"),
]