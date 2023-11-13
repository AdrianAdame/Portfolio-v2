from django.shortcuts import render, redirect

from .forms import ExperienceForm
from .models import Experience
# Create your views here.

def experiences(request):
    experiences= Experience.objects.all()

    context_data = {
        'experiences' : experiences
    }

    return render(request, "experiences/experiences_list.html", context = context_data)

def experience_new(request):
    form = None

    if request.method == "POST":
        form = ExperienceForm(request.POST)

        if form.is_valid():
            experience = form.save()

            return redirect('experiences')
    else:
        form = ExperienceForm()
    
    context_data = {
        'form' : form
    }

    return render(request, "experiences/experience_new.html", context = context_data)