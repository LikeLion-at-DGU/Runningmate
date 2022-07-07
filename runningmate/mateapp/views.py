from django.shortcuts import render, redirect, get_object_or_404
from users.models import Profile
from .models import *
from datetime import datetime
from django.shortcuts import render, redirect
from users.models import Profile
import json
import datetime
from django.http import JsonResponse
import sys, os 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from addproject import models

def showmain(request):
    calendar = Calendar.objects.filter(writer=request.user, endday__contains=datetime.date.today(
    )).order_by('endday')  # 글을 작성한 유저의 캘린더 정보만 가져오겠다. 가까운 날짜 순으로 정렬
    project = Project.objects.all()
    return render(request, 'mateapp/mainpage.html', {'calendar': calendar, 'project':project})

def showevent(request):
    if request.method == 'POST':
        date_num = json.loads(request.body)
        year = datetime.date.today().year
        month = datetime.date.today().month
        calendar = Calendar.objects.filter(writer=request.user, endday__contains=datetime.date(
            year, month, int(date_num))).order_by('endday')
        if calendar.count() != 0:

            if calendar.count() == 1:
                c0_title = calendar[0].title
                c0_startday = calendar[0].startday
                c0_endday = calendar[0].endday
                c0_starttime = calendar[0].starttime
                c0_endtime = calendar[0].endtime
                c0_place = calendar[0].place
                c1_title = None
                c1_startday = None
                c1_endday = None
                c1_starttime = None
                c1_endtime = None
                c1_place = None
            elif calendar.count() > 1:
                c0_title = calendar[0].title
                c0_startday = calendar[0].startday
                c0_endday = calendar[0].endday
                c0_starttime = calendar[0].starttime
                c0_endtime = calendar[0].endtime
                c0_place = calendar[0].place
                c1_title = calendar[1].title
                c1_startday = calendar[1].startday
                c1_endday = calendar[1].endday
                c1_starttime = calendar[1].starttime
                c1_endtime = calendar[1].endtime
                c1_place = calendar[1].place
            context = {
                "status": "exist",
                "title1": c0_title,
                "startday1": c0_startday,
                "endday1": c0_endday,
                "starttime1": c0_starttime,
                "endtime1": c0_endtime,
                "place1": c0_place,
                "title2": c1_title,
                "startday2": c1_startday,
                "endday2": c1_endday,
                "starttime2": c1_starttime,
                "endtime2": c1_endtime,
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

def create_schedule(request):
    new_schedule = Calendar.objects.filter(writer=request.user)
    new_schedule.save()
    return render(request, 'mateapp/create_schedule.html')

def calendar(request):
    calendar = Calendar.objects.filter(writer=request.user)  # 글을 작성한 유저의 캘린더 정보만 가져오겠다. 가까운 날짜 순으로 정렬
    projects = Project.objects.all() # 모델을 전부 불러옴 
    todos_list = [] # 빈리스트를 만듬 , 담아서 렌더링하는 경우가 많음
    todos = Todo.objects.all()
    todos_list.append(todos) # 그 프로젝트의 등록된 투두를 불러와서 그걸 넣은거임 
        # 보내고 싶은거 리스트로 보내서 장고나 뭐든 저런식으로 할 일이 많음
        # 알아두기
    return render(request, 'mateapp/calendar.html', {'todos_list':todos_list, 'projects':projects, 'calendar':calendar})
    # 리스트 자체를 렌더링함

def timetable(request):
    if request.method == "POST":
        # Profile에서 요청받은 user의 정보만 불러옴
        profile = Profile.objects.get(user=request.user)
        profile.timetable = request.FILES.get('timetable')
        profile.save(update_fields=['timetable'])
    return redirect('mateapp:showmain')  # render 보단 redirect 가 낫다.

def project_name(request):
    return render(request, 'mateapp/project.html')