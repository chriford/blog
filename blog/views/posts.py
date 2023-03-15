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
)
from blog.forms import PostForm


@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def post_create(request):
    if request.method == 'POST':
        post_create_form = PostForm(request.POST)
        if post_create_form.is_valid():
            post = post_create_form.save(commit=False)
            post.cleaned_data['owner'] = request.user
            post.save(commit=True)
            return redirect('blog:post-create')

    posts = Post.objects.all()
    context = {
        'post_form': PostForm,
        'posts': posts,
    }
    return render(request, 'blog/posts.html', context)

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def posts(request):
    posts = Post.objects.all()
    context = {
        'post_form': PostForm,
        'posts': posts,
    }
    return render(request, 'blog/posts.html', context)


# post_update
def post_delete(request, title, pk):
    context = {}
    return HttpResponse(f"{title}-pk will be deleted")
# def management(request):
#     context = {}
#     return render(request, 'blog/management.html', context)


def management(request):
    context = {}
    return render(request, 'blog/management.html', context)

