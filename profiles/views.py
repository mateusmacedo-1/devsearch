from django.shortcuts import redirect, render

from django.contrib import messages

from django.db.models import Q

from django.contrib.auth.decorators import login_required

from profiles.forms import MessageForm, SkillForm

from .models import Profile
from projects.models import Project

def profiles(request):
    search_query = request.GET.get('search_query', '')
    profiles = Profile.objects.filter(
        Q(name__icontains=search_query) | 
        Q(bio__icontains=search_query)  |
        Q(short_intro__icontains=search_query) |
        Q(skill__name__icontains=search_query)
    )
    context = {'profiles': profiles, 'search_query': search_query}
    return render(request, 'profiles/list.html', context)

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    projects = Project.objects.filter(owner=pk)
    context = {'profile': profile, 'projects': projects}
    return render(request, 'profiles/detail.html', context)


@login_required(login_url="accounts:login")
def inbox(request):
    profile = request.user.profile
    messages = profile.messages.all()
    unread_messages_length = profile.messages.filter(is_read=False).count()
    context = {'profile': profile, 'inbox_messages': messages, 'unread_messages_length': unread_messages_length}
    return render(request, 'profiles/inbox.html', context)

@login_required(login_url="accounts:login")
def message(request, pk):
    profile = request.user.profile
    message = profile.messages.get(pk=pk)
    message.is_read = True
    message.save()
    context = {'message': message}
    return render(request, 'profiles/message.html', context)

def create_message(request, pk):
    recipient = Profile.objects.get(pk=pk)
    sender = request.user.profile if request.user.is_authenticated else None
    form = MessageForm(recipient=recipient, sender=sender)

    if request.method == 'POST':
        form = MessageForm(request.POST, sender=sender, recipient=recipient)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user.profile
            message.save()
            return redirect('profiles:get', pk=pk)
    
    context = {'form': form, 'recipient': recipient, 'sender': sender}
    return render(request, 'profiles/message-form.html', context)

@login_required(login_url="accounts:login")
def personal_profile(request):
    profile = request.user.profile
    projects = profile.project_set.all()
    context = {'profile': profile, 'projects': projects}
    return render(request, 'profiles/personal-detail.html', context)

@login_required(login_url="accounts:login")
def create_skill(request):

    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = request.user.profile
            skill.save()
            return redirect('profiles:personal')
    
    context = {'form': form}
    return render(request, 'profiles/skill-form.html', context)

@login_required(login_url="accounts:login")
def edit_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(pk=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('profiles:personal')
    
    context = {'form': form}
    return render(request, 'profiles/skill-form.html', context)
    
@login_required(login_url="accounts:login")
def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(pk=pk)

    if request.method == 'POST':
        skill.delete()
        return redirect('profiles:personal')
    
    context = {'object': skill}
    return render(request, 'delete.html', context)