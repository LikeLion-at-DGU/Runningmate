from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from datetime import *
import json
from django.http import JsonResponse


def newproject(request):
    return render(request, 'addproject/newproject.html')
    
def createproject(request):
    new_post = Project()
    new_post.title = request.POST.get('title')
    new_post.body = request.POST.get('body')
    new_post.save()
    return render(request, 'mateapp/showmain.html', 'mateapp/calendar.html', 'mateapp/create_schedule.html')

def showproject(request):
    if request.method == 'POST':
        date_num = json.loads(request.body)
        year = datetime.date.today().year
        month = datetime.date.today().month
        project = Project.objects.filter(writer=request.user, endday__contains=datetime.date(
            year, month, int(date_num))).order_by('endday')
  
        if project.count() == 1:
            p0_title = project[0].title
            p0_startday = project[0].startday
            p0_endday = project[0].endday
            p0_body = project[0].body
            p1_title = None
            p1_startday = None
            p1_endday = None
            p1_body = None
            context = {
            "status": "exist1",
            "title1": p0_title,
            "startday1": p0_startday,
            "endday1": p0_endday,
            "body1" : p0_body,
            "title2": p1_title,
            "startday2": p1_startday,
            "endday2": p1_endday,
            "body2" : p1_body,
        }
        elif project.count() == 2:
            p0_title = project[0].title
            p0_startday = project[0].startday
            p0_endday = project[0].endday
            p0_body = project[0].body
            p1_title = project[1].title
            p1_startday = project[1].startday
            p1_endday = project[1].endday
            p1_body = project[1].body
            context = {
            "status": "exist2",
            "title1": p0_title,
            "startday1": p0_startday,
            "endday1": p0_endday,
            "body1" : p0_body,
            "title2": p1_title,
            "startday2": p1_startday,
            "endday2": p1_endday,
            "body2" : p1_body,
        }
        
        else:
            context = {"status": "null"}
        return JsonResponse(context)