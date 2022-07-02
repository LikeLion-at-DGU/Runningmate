from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from users.models import Profile
from .models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer
from .models import Calendar
import json, datetime
from django.http import JsonResponse

def showmain(request):
    calendar = Calendar.objects.filter(writer=request.user,datetime__contains=datetime.date.today()).order_by('datetime') # 글을 작성한 유저의 캘린더 정보만 가져오겠다. 가까운 날짜 순으로 정렬
    return render(request,'mateapp/mainpage.html', {'calendar':calendar})


def showevent(request):
    if request.method == 'POST':
        date_num = json.loads(request.body)
        year = datetime.date.today().year
        month = datetime.date.today().month
        calendar = Calendar.objects.filter(writer=request.user, datetime__contains=datetime.date(year, month, int(date_num))).order_by('datetime')
        
        if calendar.length != 0:
            
            if calendar.length == 1:
                c0_title = calendar[0].title
                c0_datetime = calendar[0].datetime
                c1_title = None
                c1_datetime = None
            elif calendar.length > 0:
                c0_title = calendar[0].title
                c0_datetime = calendar[0].datetime
                c1_title = calendar[1].title
                c1_datetime = calendar[1].datetime
            context = {
                "status": "exist",
                "title1": c0_title,
                "datetime1": c0_datetime,
                "title2": c1_title,
                "datetime2": c1_datetime,
            }
        else:
            context = {"status": "null"}
        return JsonResponse(context)



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


def checklist(request):
    _todos = Todo.objects.all()
    return render(request, 'mateapp/checklist.html', {'todos': _todos})


def create_todo(request):
    content = request.POST['todocontent']
    new_todo = Todo(title=content)
    new_todo.save()
    return HttpResponseRedirect(reverse('checklist'))


def delete_todo(request):
    _id = request.GET['todoNum']
    todo = Todo.objects.get(id=_id)
    todo.delete()
    return HttpResponseRedirect(reverse('checklist'))

@api_view(["GET"])
def todolist(req):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def todocreate(req):
    serializer = TodoSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(["DELETE"])
def tododelete(req, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response("Delete Success")


@api_view(["PUT"])
def todoupdate(req, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)