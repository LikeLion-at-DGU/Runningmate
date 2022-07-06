from django.shortcuts import render, redirect
from .models import *
from datetime import *


def addproject(request):
    return render(request, 'addproject.html')