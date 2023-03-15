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

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/posts.html')


def management(request):
    context = {}
    return render(request, 'blog/management.html', context)

