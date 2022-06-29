from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

# Create your views here.
def showmain(request):
    posts = Post.objects.all() # models.py에 저장된 모든 객체를 posts 에 저장함
    return render(request,'mateapp/mainpage.html')

def login(request):
    if request.user.is_authenticated:
        return render(request,'mateapp/mainpage.html')
    else:
        return render(request, 'mateapp/login.html')

def create(request):
    new_post = Post()
    new_post.userName = request.POST['userName']
    new_post.userAbility = request.POST['userAbility']
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('detail', new_post,id)


def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'mateapp/detail.html', {'post':post})

def calendar(request):
    return render(request,'mateapp/calendar.html')


#일짜별 캘린더 페이지 네이터
# def calendarDay(request): # 캘린더에 + 추가 하면 각 일자마다 페이지를 이동시켜버림
#     # posts = Post.objects.all()
#     posts = Post.objects.filter().order_by('-date') # posts는 객체들의 목록임 
#     paginator = Paginator(posts,1) # 하루씩 입력받아 페이지를 넘긴다는 뜻임
#     pagnum = request.GET.get('page') # 페이지에 해당하는 밸류의 키값을 반환하기 위해서 GET 요청을 함
#     posts = paginator.get_page(pagnum) # 페이지네이터에서 짜른 객체가 posts에 요청이 갈꺼고, 담길것임
#     return render(request, 'calenderDay.html', {'posts':posts})