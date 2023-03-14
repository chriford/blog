from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage, get_connection

from security.models import User, Profile
from security.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        user_create_form = UserCreationForm(request.POST)
        if user_create_form.is_valid():
            user = user_create_form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            messages.success(request, "Credentials have been sent to your email address")
            return redirect('blog:posts')
        else:
            return redirect('security:signup')   
    context = {
        "user_create_form": UserCreationForm, 
    }
    return render(request, 'auth/signup.html', context)

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('identifier', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Logged in successfully")
            return redirect('/')
        else:
            return redirect('/login/')
    context = {}
    return render(request, 'auth/signin.html', context)

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def signout(request):
    logout(request)
    messages.add_message(request, messages.INFO, "You have been logged out")
    return redirect(settings.LOGIN_REDIRECT_URL)
        
def profile(request):
    context = {}
    return render(request, 'auth/profile.html', context)

def password_reset(request):
    if request.method == "POST": 
        # with get_connection(host=settings.EMAIL_HOST, port=settings.EMAIL_PORT,  username=settings.EMAIL_HOST_USER, password=settings.EMAIL_HOST_PASSWORD, use_tls=settings.EMAIL_USE_TLS) as connection:  
        subject = 'CODE'
        email_from = settings.EMAIL_HOST_USER
        email_to = settings.EMAIL_HOST_USER
        recipient_list = [email_to]  
        message = 'request.POST.get("message") script sent from the blog app'  
        send_mail(
            subject, 
            message, 
            email_from, 
            recipient_list, 
            fail_silently=False,
        )
        msg = EmailMessage(subject,
            message, 
            to=recipient_list)
        msg.send()
    
        return redirect('blog:posts')
    
    context = {}
    return render(request, 'auth/forgot_password.html', context)
