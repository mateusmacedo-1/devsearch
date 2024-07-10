from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def login_view(request):

    if request.user.is_authenticated:
        return redirect('profiles:list')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        check_user_exists(username, request)

        user = authenticate(request, username=username, password=password)
        right_credentials = user is not None
        
        if right_credentials:
            login(request, user)
            return redirect('projects:list')
        else:
            messages.error(request, 'Username or password incorrect.')
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def signup(request):
    return render(request, 'accounts/signup.html')

def check_user_exists(username, request):
    try:
        User.objects.get(username=username)
    except:
        messages.error(request, 'User does not exists')