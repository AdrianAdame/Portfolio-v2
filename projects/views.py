from django.shortcuts import render

from projects.forms import ProjectForm
# Create your views here.

def projects(request):
    return render(request, "projects/projects_list.html")

def project_new(request):
    context_data = {
        'form' : ProjectForm
    }

    return render(request, "projects/project_new.html", context_data)