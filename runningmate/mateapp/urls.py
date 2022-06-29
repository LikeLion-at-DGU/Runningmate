from django.urls import path
from .views import *
app_name = "mateapp"
urlpatterns = [
    path('mainpage',showmain, name = "showmain"),
    path('calendar',calendar, name = "calendar"),
    path('detail/<int:id>', detail, name = "detail"), # 아마 여기를 페이지 넘버별로 일정이 달라지는 식으로 구현하고 싶긴한데 ..
    path('', login, name="login"),
    path('create_my_profile', create,name="create"),
]