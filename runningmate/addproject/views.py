from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from datetime import *



def newproject(request):
    return render(request, 'addproject/newproject.html')
    
def createproject(request):
    new_project = Project()
    new_project.title = request.POST.get('title') # 과목명
    new_project.body = request.POST.get('body') # 프로젝트명 
    new_project.startday = request.POST.get('startday') # 프로젝트 시작일을 받음
    new_project.endday = request.POST.get('endday') # 프로젝트 마감일을 받음
    new_project.writer = request.user
    new_project.color = request.POST.get('color')
    
    new_project.save()
    new_project.followers.add(request.user)
    for i in range(1,7):
        a = request.POST.get(f"teammate{i}")
        if a:
            new_project.followers.add(User.objects.get(username=a))


    return redirect('mateapp:showmain')

def project(request):
    projects = Project.objects.all()
    return render(request, 'mateapp/mainpage.html', {'projects': projects})