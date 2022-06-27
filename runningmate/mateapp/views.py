from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def showmain(request):
    return render(request,'mateapp/mainpage.html')

def login(request):
    if request.user.is_authenticated:
        return render(request,'mateapp/mainpage.html')
    else:
        return render(request, 'mateapp/login.html')

def calendar(request):
    return render(request,'mateapp/calendar.html')
