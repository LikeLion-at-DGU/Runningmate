from django.urls import path, include
from .views import *
from . import views

app_name = "addproject"
urlpatterns = [
    path('createproject/', views.createproject, name="createproject"),
    path('detailproject/<str:post_id>', views.detailproject, name="detailproject"),
    path('newproject/',newproject,name='newproject'),
]
