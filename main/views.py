from django.shortcuts import render, get_object_or_404
from .models import *

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'blogs':blogs})

def blog_single(request, pk):
    post = get_object_or_404(Blog, id=pk)
    return render(request, 'blog_single.html', {'post':post})

def contact(request):
    return render(request, 'contact.html')

def course(request):
    return render(request, 'course.html')