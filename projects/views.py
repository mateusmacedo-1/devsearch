from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def projects(request):
    print(request)
    return render(request, 'projects/multiple-projects.html')

def project(request, pk):
    context = {
        'pk': str(pk)
    }
    return render(request, 'projects/single-project.html', context)