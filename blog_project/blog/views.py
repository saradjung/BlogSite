from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def getBlog(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'singleblog.html',{'post':post})

def postBlog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        if title and content and author:
            Post.objects.create(title=title, content=content, author=author)
            return redirect('home')
    return render(request, 'postblog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')