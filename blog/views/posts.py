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
                messages.success("New blog created successfully")
                return redirect('blog:post-forms-page')
            else:
                messages.error("Blog creation failed due to invalid blog form")
                return redirect('blog:post-forms-page')
                
        elif form_arg == 'category-create-form':
            category_create_form = CategoryForm(request.POST)
            if category_create_form.is_valid(): 
                category = category_create_form.save(commit=True)
                category.owner = request.user
                category.save()
                messages.success("New category created successfully")
                return redirect('blog:post-forms-page')
            else:
                messages.error("Blog creation failed due to invalid category form")
                return redirect('blog:post-forms-page')

    return redirect('blog:post-forms-page')

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
            messages.info(request, f"Welcome to the blog community {user.username}!")
        else:
            pass
    else:
        pass
    posts = Post.objects.all()
    context = {
        'post_form': PostForm,
        'category_form': CategoryForm,
        'posts': posts,
    }
    return render(request, 'blog/posts.html', context)

def post_view(request, title: str, pk: int, *args, **kwargs):
    post_obj = Post.objects.filter(
        title=title,
    ).get(pk=pk)
    context = {
        'post_form': PostForm,
        'post': post_obj,
    }
    return render(request, 'blog/post-view.html', context)


def post_delete(request, title: str, pk: int, status: str, *args, **kwargs):
    post  = Post.objects.filter(
        pk=pk,
        title=title,
    ).first()
    if status == 'temporal':
        post.is_deleted = True
        post.save(
            update_fields=(
                'is_active',
                'is_deleted',
                'delete_on',
            )
        )
        messages.success(f"Blog post disabled successfully!")
        return redirect('blog:post-forms-page') # should redirect to the blog management page
    
    elif status == 'permanet':
        post.delete()    
        messages.success(f"Blog post deleted successfully!")
        return redirect('blog:post-forms-page') # should redirect to the blog management page

    else:
        pass
    
def post_update(request, title: str = None, pk: int = 0, form_arg: str = None, *args, **kwargs):
    """Updates a blog post queried by provide parameters:
        title: str
        pk: int
        form_arg: str
    """
    blog_post  = Post.objects.filter(
        pk=pk,
        title=title,
    ).first()
    if request.method == 'POST':
        if form_arg == 'post-update-form':
            blog_post_form = PostForm(
                request.POST,
                request.FILES,
                instance=blog_post,
                data=request.data,
            )
            if blog_post_form.is_valid():
                post = blog_post_form.save(commit=True)
                post.owner = request.user
                post.save()
                messages.success("blog post updated successfully")
                return redirect('blog:post-forms-page')
            else:
                messages.error("blog post creation failed due to invalid blog post form")
                return redirect('blog:post-forms-page')

        elif form_arg == 'category-update-form' and title == '00':
            category_update_form = CategoryForm(request.POST)
            if category_update_form.is_valid(): 
                category = category_update_form.save(commit=True)
                category.save()
                messages.success("category updated successfully")
                return redirect('blog:post-forms-page')
            else:
                messages.error("category update failed due to invalid category form")
                return redirect('blog:post-forms-page')
        else:
            pass
    messages.info(request, "redirected from forbidden page")
    return redirect('blog:post-forms-page') # should redirect to the blog management page

def management(request):
    context = {}
    return render(request, 'blog/management.html', context)

