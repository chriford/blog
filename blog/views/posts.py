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

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def posts(request):
    return render(request, 'blog/posts.html')
