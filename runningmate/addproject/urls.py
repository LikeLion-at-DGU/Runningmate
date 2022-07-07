from django.urls import path, include
from .views import *
from . import views

app_name = "addproject"
urlpatterns = [
    path('createproject/', views.createproject, name="createproject"),
    path('newproject/',newproject,name='newproject'),
]
