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
    Trash,
    Favorite,
    Comment,
)
from blog.forms import (
    PostForm,
    CategoryForm,
)
from security.models import (
    User,
)

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def model_form_data_create(request, form_arg: str):
    if request.method == 'POST':
        if form_arg == 'post-create-form':
            post_create_form = PostForm(request.POST)
            if post_create_form.is_valid():
                post = post_create_form.save(commit=True)
                post.owner = request.user
                post.save()
                return redirect('blog:post-forms-page')

        elif form_arg == 'category-create-form':
            category_create_form = CategoryForm(request.POST)
            # if category_create_form.is_valid(): 
            category = category_create_form.save(commit=True)
            category.owner = request.user
            category.save()
            return redirect('blog:post-forms-page')
    return HttpResponse("not a post method")

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def post_forms_page(request):
    posts = Post.objects.all()
    context = {
        'category_form': CategoryForm,
        'post_form': PostForm,
        'posts': posts,
    }
    return render(request, 'blog/post-create.html', context)

def posts(request):
    if request.user.is_authenticated:
        if request.user.is_first_time_login:
            user = User.objects.get(
                pk=request.user.pk
            )
            user.is_first_time_login = False
            user.save()
            messages.info(f"Welcome to the blog community {user.username}")
    posts = Post.objects.all()
    context = {
        'post_form': PostForm,
        'category_form': CategoryForm,
        'posts': posts,
    }
    return render(request, 'blog/posts.html', context)

def post_view(request, title, pk, *args, **kwargs):
    post_obj = Post.objects.filter(
        title=title,
    ).get(pk=pk)
    context = {
        'post_form': PostForm,
        'post': post_obj,
    }
    return render(request, 'blog/post-view.html', context)


def post_delete(request, title, pk, *args, **kwargs):
    post  = Post.objects.filter(
        pk=pk,
        title=title,
    ).first()
    post.is_deleted = True
    post.save(
        update_fields=(
            'is_active',
            'is_deleted',
            'delete_on',
        )
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

