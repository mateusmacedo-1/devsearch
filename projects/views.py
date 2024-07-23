from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from django.db.models import Q
from projects.forms import ProjectForm
from projects.utils import get_int_param, get_page_param
from .models import Project
# Create your views here.

def projects(request):

    search_query = request.GET.get('search_query', '')
    page_len = get_int_param(request, 'page_len', 3)

    projects = Project.objects.filter(
        Q(title__icontains=search_query) | 
        Q(description__icontains=search_query)  |
        Q(owner__name__icontains=search_query)  |
        Q(tags__name__icontains=search_query)
    )
    paginator = Paginator(projects, page_len)

    page = get_page_param(request, 'page', 1, paginator.num_pages)
    projects_page = paginator.page(page)
        
    context = {
        'projects': projects_page, 'search_query': search_query, 'paginator': paginator
    }

    return render(request, 'projects/list.html', context)

def project(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/detail.html', context)

@login_required(login_url="accounts:login")
def create_project(request):
    
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user.profile
            project.save()
            return redirect('profiles:personal')
    
    context = {'form': form}
    return render(request, 'projects/form.html', context)

@login_required(login_url="accounts:login")
def edit_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(pk=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:list')
    context = {'form': form}
    return render(request, 'projects/form.html', context)

@login_required(login_url="accounts:login")
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(pk=pk)
    context = {'object': project}
    if request.method == 'POST':
        project.delete()
        return redirect('projects:list')
    return render(request, 'delete.html', context)