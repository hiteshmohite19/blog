from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def home(request):
    data = Blog.new_manager.all()

    content={
        'posts':data,
        'title':'Home'
    }

    return render(request,'blog/home.html',content)


def single_blog(request,blog):

    data = get_object_or_404(Blog,slug=blog,status='published')
    content={
        'post':data,
        'title':'Blog'
    }

    return render(request, 'blog/blog.html',content)