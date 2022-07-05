from django.urls import path, include
from .views import *

app_name = "addproject"
urlpatterns = [
    path('addproject/', addproject, name='addproject'),
]