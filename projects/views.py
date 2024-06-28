from django.shortcuts import render, redirect

from projects.forms import ProjectForm
from .models import Project
# Create your views here.

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/list.html', context)

def project(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/detail.html', context)

def create_project(request):
    form = ProjectForm()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects:all')
    
    context = {'form': form}
    return render(request, 'projects/form.html', context)

def edit_project(request, pk):
    project = Project.objects.get(pk=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:all')
    context = {'form': form}
    return render(request, 'projects/form.html', context)

def delete_project(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    if request.method == 'POST':
        project.delete()
        return redirect('projects:all')
    return render(request, 'projects/delete.html', context)