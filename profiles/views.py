from django.shortcuts import render

from .models import Profile
from projects.models import Tag

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'profiles/list.html', context)
