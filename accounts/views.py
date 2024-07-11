from django.shortcuts import render, redirect

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from accounts.forms import CustomUserCreationForm

# Create your views here.
def login_view(request):

    if request.user.is_authenticated:
        return redirect('profiles:list')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        right_credentials = user is not None
        
        if right_credentials:
            login(request, user)
            messages.success(request, 'User authenticated!')
            return redirect('projects:list')
        else:
            messages.error(request, 'Username or password incorrect.')
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'User logout')
    return redirect('accounts:login')

def signup(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User created.")
            login(request, user)
            return redirect('profiles:list')
        else:
            messages.error(
                request, 'An error has occurred during registration')
    # renderiza no final, pois caso de erros, esse obj q tem os erros
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
