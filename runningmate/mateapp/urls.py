from django.urls import path
from .views import *
app_name = "mateapp"
urlpatterns = [
    path('',showmain, name = "showmain"),
]