from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        check_user_exists(username)

        user = authenticate(request, username=username, password=password)
        right_credentials = user is not None
        
        if right_credentials:
            login(request, user)
            return redirect('projects:all')
        else:
            print('Username or password incorrect.')
    
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def signup(request):
    return render(request, 'accounts/signup.html')

def check_user_exists(username):
    try:
        User.objects.get(username=username)
    except:
        print('User does not exists')