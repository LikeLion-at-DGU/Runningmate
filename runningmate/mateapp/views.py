from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from users.models import Profile


def showmain(request):
    return render(request,'mateapp/mainpage.html')


def login(request):
    if request.user.is_authenticated:
        return render(request,'mateapp/mainpage.html')
   
    else:
        return render(request,'account/login.html')


def calendar(request):
    return render(request,'mateapp/calendar.html')


def timetable(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user) # Profile에서 요청받은 user의 정보만 불러옴
        profile.timetable = request.FILES.get('timetable')
        profile.save(update_fields=['timetable'])
    return redirect('mateapp:showmain') # render 보단 redirect 가 낫다.
