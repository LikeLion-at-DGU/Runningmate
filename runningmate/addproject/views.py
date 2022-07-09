from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from datetime import *



def newproject(request):
    return render(request, 'addproject/newproject.html')
    
def createproject(request):
    new_project = Project()
    new_project.title = request.POST.get('title')
    new_project.body = request.POST.get('body')
    new_project.startday = request.POST.get('startday')
    new_project.endday = request.POST.get('endday')
    new_project.save()
    return redirect('mateapp:showmain')

def project(request):
    projects = Project.objects.all()
    return render(request, 'mateapp/mainpage.html', {'projects': projects})