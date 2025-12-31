from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'blog/home.html')

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})
    