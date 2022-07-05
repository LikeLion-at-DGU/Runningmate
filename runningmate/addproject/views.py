from django.shortcuts import render
from .models import *

def addproject(request):
    projects = Project.objects.all()
    return render(request, 'addproject.html')