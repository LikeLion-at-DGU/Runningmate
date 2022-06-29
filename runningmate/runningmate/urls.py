from django.contrib import admin
from django.urls import path, include
from mateapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mateapp.urls')),
    path('accounts/',include('allauth.urls')),
    
]
