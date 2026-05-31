from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')