from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers

app_name = "mateapp"

router = routers.DefaultRouter() # router 는 모든 모델에 대한 url 추출
router.register('', views.TodoModelViewSet) # views.py의 TodoModelViewSet에서 지원하는 여러 기능 url을 따로 지정하지 않고 불러옴

urlpatterns = [
    path('mainpage',showmain, name = "showmain"),
    path('calendar',calendar, name = "calendar"),
    path('', login, name="login"),
    path('timetable',timetable, name='timetable'),
    path('todo/', include(router.urls), name="todo"),
]