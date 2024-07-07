from django.shortcuts import render

from .models import Profile
from projects.models import Tag

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'profiles/list.html', context)

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    context = {'profile': profile}
    return render(request, 'profiles/detail.html', context)