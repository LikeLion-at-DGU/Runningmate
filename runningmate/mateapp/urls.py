from django.urls import path, include
from .views import *
# from . import views
# from addproject import *

app_name = "mateapp"
urlpatterns = [
    path('mainpage',showmain, name = "showmain"),
    path('calendar',calendar, name = "calendar"),
    path('showevent',showevent, name = "showevent"),
    path('', login, name="login"),
    path('timetable',timetable, name='timetable'),
    path('project_name/', project_name, name="project_name"),
]
