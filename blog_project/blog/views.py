from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def getBlog(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'singleblog.html',{'post':post})