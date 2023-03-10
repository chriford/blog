from django.shortcuts import render

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        ...        
    context = dict()
    return render(request, 'auth/signin.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        account_type = request.POST.get('account-type', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        ...
    context = dict()
    return render(request, 'auth/signup.html', context)

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        ...
    context = dict()
    return render(request, 'auth/forgot_password.html', context)

