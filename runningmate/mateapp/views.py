from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def showmain(request):
    return render(request,'mateapp/mainpage.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('mateapp/showmain')
        else:
            return render(request, 'mateapp/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'mateapp/login.html')

def calendar(request):
    return render(request,'mateapp/calendar.html')
