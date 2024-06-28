from django.shortcuts import render

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
    context = {'form': form}
    return render(request, 'projects/form.html', context)