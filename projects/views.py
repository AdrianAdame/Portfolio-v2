from django.shortcuts import render, redirect

from .forms import ProjectForm
from .models import Project
# Create your views here.

def projects(request):
    projects = Project.objects.all()

    context_data = {
        'projects': projects
    }
    return render(request, "projects/projects_list.html", context=context_data)

def project_new(request):
    form = None
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save()

            return redirect('projects')
    else:
        form = ProjectForm()

    context_data = {
        'form': form
    }

    return render(request, "projects/project_new.html", context=context_data)
