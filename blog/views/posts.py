import os

from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    HttpResponse,     
    redirect,
    HttpResponseRedirect,
)
from blog.models import (
    Post,
    Favorite,
    Comment,
)
from blog.forms import PostForm


@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def post_create(request):
    if request.method == 'POST':
        post_create_form = PostForm(request.POST)
        if post_create_form.is_valid():
            post = post_create_form.save(commit=True)
            post.owner = request.user
            post.save()
            return redirect('blog:post-create')

    posts = Post.objects.all()
    context = {
        'post_form': PostForm,
        'posts': posts,
    }
    return render(request, 'blog/post-create.html', context)

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def posts(request):
    posts = Post.objects.all()
    context = {
        'post_form': PostForm,
        'posts': posts,
    }
    return render(request, 'blog/posts.html', context)


def post_delete(request, title, pk, *args, **kwargs):
    post  = Post.objects.filter(
        pk=pk,
        title=title,
    )
    return HttpResponse(f"{title}-pk will be deleted")

def post_update(request, title, pk, *args, **kwargs):
    post  = Post.objects.filter(
        pk=pk,
        title=title,
    )
    return HttpResponse(f"{title}-pk will be updated")

def management(request):
    context = {}
    return render(request, 'blog/management.html', context)

