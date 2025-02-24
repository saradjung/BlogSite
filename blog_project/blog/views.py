from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def getBlog(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'singleblog.html',{'post':post})

@login_required(login_url='/login/')
def postBlog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        if title and content:
            Post.objects.create(title=title, content=content, author=author)
            return redirect('home')
    return render(request, 'postblog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def userlogin(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"Login successful")
            next_url = request.GET.get('next','home')
            return redirect(next_url)
        else:
            messages.error(request,"Invalid username or password")

    return render(request, "login.html")

def logout(request):
    return HttpResponse('Log Out')