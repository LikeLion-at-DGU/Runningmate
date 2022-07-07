from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from datetime import *


def newproject(request):
    return render(request, 'addproject/newproject.html')
    
def createproject(request):
    new_post = Project()
    new_post.title = request.POST.get('title')
    new_post.body = request.POST.get('body')
    new_post.save()
    return redirect('mateapp:showmain')

def detailproject(request, post_id):
    post = get_object_or_404(Project, pk = post_id)
    return render(request,'addproject/detailproject.html', {'post':post})