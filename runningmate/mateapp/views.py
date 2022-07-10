from django.shortcuts import render, redirect, get_object_or_404
from users.models import Profile
from .models import *
from addproject.models import *
from datetime import datetime
from django.shortcuts import render, redirect
from addproject.models import *
import json
import datetime
from django.http import JsonResponse
from addproject.models import *
from users import *
import sys, os 
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from addproject import models
from django.core.paginator import Paginator

def showmain(request):
    calendar = Calendar.objects.filter(writer=request.user, endday__contains=datetime.date.today(
    )).order_by('endday')  # 글을 작성한 유저의 캘린더 정보만 가져오겠다. 가까운 날짜 순으로 정렬
    projects = Project.objects.filter(followers=request.user)
    profile = Profile.objects.all()
    posts = Post.objects.all().order_by('-day')
    return render(request, 'mateapp/mainpage.html', {'calendar': calendar, 'projects':projects,'posts':posts, })


def showevent(request):
    if request.method == 'POST':
        date_num = json.loads(request.body)
        year = datetime.date.today().year
        month = datetime.date.today().month
        calendar = Calendar.objects.filter(writer=request.user, endday__contains=datetime.date(
            year, month, int(date_num))).order_by('endday')
  
        if calendar.count() == 1:
            c0_title = calendar[0].title
            c0_startday = calendar[0].startday
            c0_endday = calendar[0].endday
            c0_starttime = calendar[0].starttime
            c0_endtime = calendar[0].endtime
            c0_place = calendar[0].place
            c0_body = calendar[0].body
            c0_color = calendar[0].color
            c1_title = None
            c1_startday = None
            c1_endday = None
            c1_starttime = None
            c1_endtime = None
            c1_place = None
            c1_body = None
            c1_color = None
            context = {
            "status": "exist1",
            "title1": c0_title,
            "startday1": c0_startday,
            "endday1": c0_endday,
            "starttime1": c0_starttime,
            "endtime1": c0_endtime,
            "place1": c0_place,
            "body1" : c0_body,
            "color1" : c0_color,
            "title2": c1_title,
            "startday2": c1_startday,
            "endday2": c1_endday,
            "starttime2": c1_starttime,
            "endtime2": c1_endtime,
            "place2": c1_place,
            "body2" : c1_body,
            "color2" : c1_color,
        }
        elif calendar.count() >= 2:
            c0_title = calendar[0].title
            c0_startday = calendar[0].startday
            c0_endday = calendar[0].endday
            c0_starttime = calendar[0].starttime
            c0_endtime = calendar[0].endtime
            c0_place = calendar[0].place
            c0_body = calendar[0].body
            c0_color = calendar[0].color
            c1_title = calendar[1].title
            c1_startday = calendar[1].startday
            c1_endday = calendar[1].endday
            c1_starttime = calendar[1].starttime
            c1_endtime = calendar[1].endtime
            c1_place = calendar[1].place
            c1_body = calendar[1].body
            c1_color = calendar[1].color
            context = {
            "status": "exist2",
            "title1": c0_title,
            "startday1": c0_startday,
            "endday1": c0_endday,
            "starttime1": c0_starttime,
            "endtime1": c0_endtime,
            "place1": c0_place,
            "body1" : c0_body,
            "color1" : c0_color,
            "title2": c1_title,
            "startday2": c1_startday,
            "endday2": c1_endday,
            "starttime2": c1_starttime,
            "endtime2": c1_endtime,
            "place2": c1_place,
            "body2" : c1_body,
            "color2" : c1_color,
        }
        
        else:
            context = {"status": "null"}
        return JsonResponse(context)




def login(request):
    if request.user.is_authenticated:
        projects = Project.objects.all()
        return render(request, 'mateapp/mainpage.html', {'projects':projects})

    else:
        return render(request, 'account/login.html')

def create_schedule(request):
    projecttitles = Project.objects.filter(writer=request.user)
    if request.method == 'POST':
        new_schedule = Calendar()
        new_schedule.title = request.POST['title']
        new_schedule.writer = request.user
        new_schedule.body = request.POST['body']
        new_schedule.startday = request.POST.get('startday')        
        new_schedule.endday = request.POST.get('endday')
        new_schedule.starttime = request.POST.get('starttime')
        new_schedule.endtime = request.POST.get('endtime')
        new_schedule.place = request.POST['place']
        new_schedule.color = request.POST['color']
        new_schedule.save()
        return redirect('mateapp:calendar')
    else :
        new_schedule = Calendar.objects.all()
        return render(request, 'mateapp/create_schedule.html',{'new_schedule':new_schedule, 'projecttitles':projecttitles})

def calendar(request):
    calendar = Calendar.objects.filter(writer=request.user)  # 글을 작성한 유저의 캘린더 정보만 가져오겠다. 가까운 날짜 순으로 정렬
    calendars = Calendar.objects.filter(writer=request.user)
    schedules_list = []
    schedules = Calendar.objects.filter(writer=request.user)
    schedules_list.append(schedules)
    # 간트차트

    projects = Project.objects.all() # 모델을 전부 불러옴
    todos_list = [] # 빈리스트를 만듬 , 담아서 렌더링하는 경우가 많음
    todos = Calendar.objects.filter(writer=request.user)
    todos_list.append(todos) # 그 프로젝트의 등록된 투두를 불러와서 그걸 넣은거임 
        # 보내고 싶은거 리스트로 보내서 장고나 뭐든 저런식으로 할 일이 많음
    #     # 알아두기
    return render(request, 'mateapp/calendar.html', {'projects':projects, 'todos_list':todos_list,'calendar':calendar, 'schedules_list':schedules_list, 'calendars':calendars})
    # 리스트 자체를 렌더링함

def timetable(request):
    if request.method == "POST":
        # Profile에서 요청받은 user의 정보만 불러옴
        profile = Profile.objects.get(user=request.user)
        profile.timetable = request.FILES.get('timetable')
        profile.save(update_fields=['timetable'])
    return redirect('mateapp:showmain')  # render 보단 redirect 가 낫다.

def project_detail(request, project_id):
    projects = Project.objects.filter(followers=request.user)
    project = Project.objects.get(pk=project_id)
    posts = Post.objects.all()
    post = Post.objects.filter(project=project)
    comment = Comment.objects.filter()
    page = int(request.GET.get('p',1))
    paginator = Paginator(post,4)
    boards = paginator.get_page(page)
    return render(request, 'mateapp/project.html', {'boards':boards, 'projects':projects,'project':project,'posts':posts, 'post':post})

# 포스트가 갖고 있는 숫자가 가장 높은걸 필터로 찾아서 오늘 날짜와 비교해서 출력함

# 게시물 CRUD

def create_post(request, project_id):
    projects = Project.objects.all()
    project = Project.objects.get(pk=project_id)
    posts = Post.objects.all()
    day = datetime.date.today()
    # post = Post.objects.get(project=project)
    if request.method == "POST":
        # project = Project.objects.get(title=project_title)
        post_title = request.POST['title']
        post_body = request.POST['body']
        Post.objects.create(title=post_title, user=request.user, project=project, body=post_body) # post는 세가지 필드가 있는데, 
        # 어떤 모델이든간에 pk가 있어야함 Foreign key는 생략이 될 수가 없음, 일대다 관계일때 쓴다는건데
        # 
    return redirect('mateapp:project_detail', project_id)
    # return render(request, 'mateapp/project.html', {'posts':posts,'projects':projects})
        

def create_comment(request, project_id, post_id):
    project = Project.objects.get(pk=project_id)
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":
        post = get_object_or_404(Post,pk=post_id) #Post로 등록된 값이 잇으면 불러오고 없으면 404 출력시킴
        content = request.POST['content']
        file = request.FILES.get('file')
        Comment.objects.create(content=content, post=post, user=request.user) # 모델=뷰
    return redirect('mateapp:post_detail', project_id, post_id)
    # id는 식별값이기 때문에 무조건 존재하는 필드임 

def post_detail(request, project_id, post_id):
    project = Project.objects.get(pk = project_id)
    post = Post.objects.get(pk = post_id)
    comments = Comment.objects.filter(post = post)
    page = int(request.GET.get('p',1))
    paginator = Paginator(comments,4)
    boards = paginator.get_page(page)
    return render(request, 'mateapp/project_post.html', {'boards':boards,'project':project, 'post':post, 'comments':comments})    
