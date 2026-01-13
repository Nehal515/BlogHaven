from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Genre
from .forms import CommentForm,PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def home(request):
    genre_slug=request.GET.get('genre')
    posts=Post.objects.all().order_by('-created_at')
    genres=Genre.objects.all()

    if genre_slug:
        posts = posts.filter(genres__slug=genre_slug)

    context={ 
        "posts":posts,
        "genres": genres,
        "active_genre": genre_slug
    }
    return render(request,'home.html',context)

def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug)
    comments=post.comments.all().order_by("-created_at")

    if request.method=="POST":

        if not request.user.is_authenticated:
            messages.error(request,"You must be logged in")
            return redirect('login')

        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.author=request.user
            comment.save()

            messages.success(request,"comment added")
            return redirect("post_detail",slug=post.slug)
    else:
        form=CommentForm()

    context={
        "post":post,
        "comments":comments,
        "form":form,
    }

    return render(request,"post_detail.html",context)

def about(request):
    return render(request,'about.html')

@login_required
def create_post(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect("post_detail",slug=post.slug)
    else:
        form=PostForm()

    context={
        "form":form,
    }

    return render(request,"create_post.html",context)

@login_required
def update_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.author != request.user:
        messages.error(request, "Not authorized")
        return redirect("post_detail", slug=slug)

    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect("post_detail", slug=post.slug)

    return render(request, "update_post.html", {"form": form})

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.author == request.user:
        post.delete()
        messages.success(request, "Post deleted")

    return redirect("home")

@login_required
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    return redirect(request.META.get("HTTP_REFERER", "home"))

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created")
            return redirect('login')
    else:
        form=UserCreationForm()

    return render(request,'register.html',{"form":form})