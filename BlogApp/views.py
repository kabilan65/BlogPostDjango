from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost, Comment
from .forms import PostForm, PostEditForm, CommentForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def home(request):
    posts = BlogPost.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('home')
    else:
        form = PostForm()


    context = {
        'posts' : posts,
        'form' : form,
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comments.all()
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            if request.user.is_authenticated:
                new_comment.author = request.user
            else:
                new_comment.author = None
            new_comment.save()
            return redirect('post_detail', pk=post.id)
    else:
        comment_form = CommentForm()

    context = {
        'post' : post,
        'comments' : comments,
        'comment_form' : comment_form,
    }
    return render(request, 'blog/post_detail.html', context)

def post_edit(request, pk):
    post = BlogPost.objects.get(id=pk)
    
    if request.method == "POST":
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = PostEditForm(instance=post)

    context = {
        'post' : post,
        'form' : form,
    }

    return render(request, 'blog/post_edit.html', context)

def post_delete(request, pk):
    post = BlogPost.objects.get(id=pk)
    post.delete()
    messages.success(request, 'Post Deleted Successfully !')
    return redirect('home')

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)

    if request.user == comment.author:
        post_id = comment.post.id
        comment.delete()
        return redirect('post_detail', pk = post_id)
    else:
        return redirect('post_detail', pk = comment.post.id)

def search_post(request):
    query = request.GET.get('q')
    if query:
        posts = BlogPost.objects.filter(Q(title__icontains=query) | Q(tags__icontains=query)
        )
    else:
        posts = BlogPost.objects.all()  

    context = {
        'posts': posts,
        'query': query,
    }
    return render(request, 'blog/search_result.html', context)