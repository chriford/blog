from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from security.models import User, Profile

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        if password.__eq__(password2):
            ...            
    context = {}
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
def logout(request):
    logout(request)
    messages.add_message(request, messages.INFO, "You have been logged out")
    return redirect(settings.LOGIN_REDIRECT_URL)
        
def profile(request):
    context = {}
    return render(request, 'auth/profile.html', context)

def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        ...
    context = {}
    return render(request, 'auth/forgot_password.html', context)
