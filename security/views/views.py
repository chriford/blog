from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage, get_connection

from security.models import User, Profile
from security.forms import UserCreationForm, UserProfileForm
from blog_utils import (
    send_email,
) 
def signup(request):
    if request.method == 'POST':
        user_create_form = UserCreationForm(request.POST)
        if user_create_form.is_valid():
            user = user_create_form.save(commit=True)
            login(request, user)
            messages.success(request, "Registration successful")
            messages.success(request, "Credentials have been sent to your email address")
            return redirect('blog:posts')
        else:
            messages.error(request, "Registration failed")
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
    context = {
            "user_create_form": UserCreationForm, 
        }
    return render(request, 'auth/signin.html', context)

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def signout(request):
    logout(request)
    messages.add_message(request, messages.INFO, "You have been logged out")
    return redirect(settings.LOGIN_REDIRECT_URL)

@login_required(login_url=settings.LOGIN_REDIRECT_URL)    
def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES or None)
        if profile_form.is_valid():
            profile_form.save(commit=True)
            messages.success(request, 'profile details updated successfully')
            return redirect('security:profile')
    context = {}
    return render(request, 'auth/profile.html', context)

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def change_password(request):
    if request.method == "POST":
        send_email(
            recipient_list=[settings.EMAIL_HOST_USER],
            subject="BLOG - Password Update",
            body="Your password has been changed successfully",
        )
        messages.success(request, "Your password has been changed successfully")
        return redirect('security:profile')
    context = {}
    return render(request, 'auth/change_password.html', context)

@login_required(login_url=settings.LOGIN_REDIRECT_URL)
def password_reset(request):
    if request.method == "POST": 
        send_email(
            recipient_list=[settings.EMAIL_HOST_USER],
            subject="BLOG - Reset Password",
            body="Click the link below to reset your password\n www.google.com",    
        )
        messages.success(request, "We have sent an email to the email you provided on registration to this platform")
        return redirect('security:forgot-password')

    context = {}
    return render(request, 'auth/forgot_password.html', context)

