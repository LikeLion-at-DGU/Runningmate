from django.shortcuts import render, redirect
from users.models import Profile
from .models import Todo
from rest_framework import viewsets
from .serializer import TodoSerializer


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

class TodoModelViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
# TodoModelViewSet은 Create, Retrieve, Update, Partial_update, Destory, List를 지원
# 별다른 함수 없이 장고에서 기능을 불러올 수 있음
