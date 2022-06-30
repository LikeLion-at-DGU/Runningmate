from winsound import MB_ICONASTERISK
from django.shortcuts import render, redirect
from runningmate.mateapp.views import timetable
from .models import Profile
# 해당앱의 views.py 에서 불러와서 Profile 모델을 불러오면 됨
# Create your views here.

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        user = request.POST['user']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        mbti = request.POST['mbti']
        intro = request.POST['intro']
        timetable = request.POST['timetable']

        res_data = {}
        if password1 != password2:
            res_data['error'] = 'differnet'
            print(res_data)
        else :
            profile = Profile(
                user = user, password1 = password1, password2 = password2, phone = phone, mbti = mbti, intro = intro, timetable = timetable,
            ) # 객체생성
            profile.save()
    return render(request, 'signup.html')
