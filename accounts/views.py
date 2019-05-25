from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        #user has info and wants to create account
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html', {'error': 'Username already has been taken.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password Must match!'})
    else:
        # user wants to enter information
        return render(request, 'accounts/signup.html')
def login(request):
    return render(request, 'accounts/login.html')
def logout(request):
    return render(request, 'accounts/signup.html')
