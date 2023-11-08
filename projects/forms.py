from django import forms

from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

        fields = [
            'name', 
            'description', 
            'year', 
            'img', 
            'repository', 
            'technologies'
        ]

        widgets = {
            'name' : forms.TextInput(attrs = {'placeholder' : 'Project Name'}),
            'description' : forms.Textarea(attrs = {'placeholder' : 'Project Description'}),
            'year' : forms.NumberInput(attrs = {'placehoder' : 'Project Creation Year'}),
            'img' : forms.ClearableFileInput(attrs = {'placeholder' : 'Select an image of the project'}),
            'repository' : forms.URLInput(attrs = {'placeholder' : 'URL Link for Github Repository'}),
        }