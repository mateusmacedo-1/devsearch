from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Profile
from projects.models import Project, Tag

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'profiles/list.html', context)

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    projects = Project.objects.filter(owner=pk)
    context = {'profile': profile, 'projects': projects}
    return render(request, 'profiles/detail.html', context)


@login_required(login_url="accounts:login")
def personal_profile(request):
    profile = request.user.profile
    projects = Project.objects.filter(owner=profile.id)
    context = {'profile': profile, 'projects': projects}
    return render(request, 'profiles/personal-detail.html', context)