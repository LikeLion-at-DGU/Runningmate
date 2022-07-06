from django.shortcuts import render, redirect, get_object_or_404
from users.models import Profile
from .models import Calendar, TodoComment, TodoTitle
from datetime import datetime
from django.shortcuts import render, redirect
from users.models import Profile
from .models import Calendar, Project
import json
import datetime
from django.http import JsonResponse
import sys, os 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from addproject import models

def showmain(request):
    calendar = Calendar.objects.filter(writer=request.user, datetime__contains=datetime.date.today(
    )).order_by('datetime')  # 글을 작성한 유저의 캘린더 정보만 가져오겠다. 가까운 날짜 순으로 정렬
    project = Project.objects.all()
    return render(request, 'mateapp/mainpage.html', {'calendar': calendar, 'project':project})

def showevent(request):
    if request.method == 'POST':
        date_num = json.loads(request.body)
        year = datetime.date.today().year
        month = datetime.date.today().month
        calendar = Calendar.objects.filter(writer=request.user, datetime__contains=datetime.date(
            year, month, int(date_num))).order_by('datetime')
        if calendar.count() != 0:

            if calendar.count() == 1:
                c0_title = calendar[0].title
                c0_datetime = calendar[0].datetime
                c0_place = calendar[0].place
                c1_title = None
                c1_datetime = None
                c1_place = None
            elif calendar.count() > 1:
                c0_title = calendar[0].title
                c0_datetime = calendar[0].datetime
                c0_place = calendar[0].place
                c1_title = calendar[1].title
                c1_datetime = calendar[1].datetime
                c1_place = calendar[1].place
            context = {
                "status": "exist",
                "title1": c0_title,
                "datetime1": c0_datetime,
                "place1": c0_place,
                "title2": c1_title,
                "datetime2": c1_datetime,
                "place2": c1_place,
            }
        else:
            context = {"status": "null"}
        return JsonResponse(context)



def login(request):
    if request.user.is_authenticated:
        return render(request, 'mateapp/mainpage.html')

    else:
        return render(request, 'account/login.html')

def calendar(request):
    todos = TodoTitle.objects.all()
    calendar = Calendar.objects.filter(writer=request.user)  # 글을 작성한 유저의 캘린더 정보만 가져오겠다. 가까운 날짜 순으로 정렬
    return render(request,'mateapp/calendar.html', {'todos':todos, 'calendar': calendar})


def todo_detail(request, id):
    todo = get_object_or_404(TodoTitle, pk = id)
    todocomments = TodoComment.objects.filter(todo=todo.id)
    return render(request, 'mateapp/calendar.html', {'todo':todo, 'todocomments':todocomments})

def todo_new(request) :
    return render(request, 'mateapp/todo_new.html')

def todo_create(request):
    new_todo = TodoTitle()
    new_todo.title = request.POST['title']
    new_todo.save()
    return redirect('mateapp:todo_detail', new_todo.id)

def todo_update(request, id):
    up_todo = TodoTitle.objects.get(id=id)
    up_todo.title = request.POST['title']
    up_todo.save()
    return redirect('mateapp:calendar')

def todo_delete(request, id):
    del_todo = TodoTitle.objects.get(id=id)
    del_todo.delete()
    return redirect('mateapp:calendar')

def todocomment_create(request, todo_id):
    new_todocomment = TodoComment()
    new_todocomment.content = request.POST['content']
    new_todocomment.post = get_object_or_404(TodoTitle, pk = todo_id)
    new_todocomment.save()
    return redirect('mateapp:calendar', todo_id)

def todocomment_update(request, todocomment_id):
    update_todocomment = get_object_or_404(TodoComment, pk = todocomment_id)
    update_todocomment.content = request.POST['content']
    update_todocomment.save()
    return redirect('mateapp:calendar')

def todocomment_delete(request, todocomment_id):
    del_todocomment = get_object_or_404(TodoComment, pk = todocomment_id)
    del_todocomment.delete()
    return redirect('mateapp:caledar')

def timetable(request):
    if request.method == "POST":
        # Profile에서 요청받은 user의 정보만 불러옴
        profile = Profile.objects.get(user=request.user)
        profile.timetable = request.FILES.get('timetable')
        profile.save(update_fields=['timetable'])
    return redirect('mateapp:showmain')  # render 보단 redirect 가 낫다.

def project_name(request):
    return render(request, 'mateapp/project.html')