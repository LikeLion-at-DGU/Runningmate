from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request,'mateapp/mainpage.html')

def calendar(request):
    return render(request,'mateapp/calendar.html')