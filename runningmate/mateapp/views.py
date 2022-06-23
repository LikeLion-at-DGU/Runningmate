from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request,'mateapp/mainpage.html')

def login(request):
    return render(request, 'mateapp/login.html')