from django.urls import path, include
from .views import *
from . import views
from runningmate import addproject

app_name = "addproject"
urlpatterns = [
    path('addproject',addproject, name = "addproject"),
]
