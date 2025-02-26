from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment, Like, Bookmark, Tag
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
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
        selected_tags = request.POST.getlist('tags')
        if title and content:
            post = Post.objects.create(title=title, content=content, author=author, image=image)
            post.tags.set(selected_tags)
            return redirect('home')
    else:
        tags = Tag.objects.all()
        return render(request, 'postblog.html', {"tags":tags})

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

@login_required
def bookmarked_posts(request):
    bookmarked_posts = Post.objects.filter(bookmarks__user=request.user)

    
    return render(request, 'bookmarks.html', {'bookmarked_posts': bookmarked_posts})

def author_posts(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author.username)  # Filter by author username
    return render(request, 'author_posts.html', {'author': author, 'posts': posts})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'all_tags.html', {"tags":tags})

def posts_by_tag(request, tag_name):
    try:
        tag = Tag.objects.get(name=tag_name)
        posts = tag.posts.all()
        return render(request, 'posts_by_tag.html', {'tag': tag, 'posts': posts})
    except:
        return redirect('error')
    
def error(request):
    return render(request,'error.html')