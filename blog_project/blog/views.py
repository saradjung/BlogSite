from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment, Like, Bookmark
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def getBlog(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user.is_authenticated:
        has_bookmarked = Bookmark.objects.filter(user=request.user, post=post).exists()
    else:
        has_bookmarked = False
    return render(request, 'singleblog.html',{'post':post, 'has_bookmarked':has_bookmarked,})

@login_required(login_url='/login/')
def postBlog(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')
        author = request.user
        if title and content:
            Post.objects.create(title=title, content=content, author=author, image=image)
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

#user logout function
def userlogout(request):
    logout(request)
    return redirect('home')

#performs user registration without super admin permission
def signup(request):
    if request.method =="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("home")
        else:
            return render(request, "signup.html", {"form": form}) 
    else:
        form=CustomUserCreationForm()

        return render(request,"signup.html",{"form":form})

#adds comments on the blog post only if user is logged in   
@login_required(login_url='/login/')
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(post=post, user=request.user, content=content)
    return redirect("blog", post_id=post.id)

#likes post only if user is logged in
@login_required(login_url='/login/')
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(user=request.user, post=post).first()

    if like:
        like.delete()  # Unlike the post
    else:
        Like.objects.create(user=request.user, post=post)  # Like the post

    return redirect('blog', post_id=post.id)  # Ensure 'single_post' is your post detail view name

#bookmark post only if used is logged in
@login_required
def bookmark_post(request, post_id):
    post =get_object_or_404(Post, id=post_id)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, post=post)

    if not created: #if already bookmarked
        bookmark.delete()
    return redirect('blog', post_id=post_id) #redirects user to the same post