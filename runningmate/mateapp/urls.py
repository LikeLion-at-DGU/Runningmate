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
    path('<int:project_id>', project_detail, name="project_detail"),
    path('<int:project_id>/<int:post_id>/create_comment', create_comment, name="create_comment"),
    path('create_schedule/',create_schedule,name="create_schedule"),
    path('<int:project_id>/create_post', create_post, name='create_post'),
    path('<int:project_id>/<int:post_id>', post_detail, name="post_detail"),
]
