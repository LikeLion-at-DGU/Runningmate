from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from users.models import Profile
from .models import Post
from django.utils import timezone


def showmain(request):
    posts = Post.objects.all()
    return render(request,'mateapp/mainpage.html', {'posts':posts})


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

def newproject(request):
    return render(request, 'mateapp/newproject.html')

def create_project(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('mateapp:detail_project',new_post.id)

def edit_project(request,id):
    edit_post = Post.objects.get(id = id)
    return render(request, 'mateapp/edit_project.html', {'post': edit_post})

def delete_project(request,id):
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('mateapp:showmain')

def detail_project(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request,'mateapp/detail_project.html', {'post':post})