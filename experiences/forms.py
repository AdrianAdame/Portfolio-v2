from django import forms

from .models import Experience


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience

        fields = [
            'entity',
            'title',
            'description',
            'period',
            'technologies'
        ]

        widgets = {
            'entity': forms.TextInput(attrs={
                'placeholder': 'Work Place of School'
            }),
            'title': forms.TextInput(attrs={
                'placeholder': 'Role or Major'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Job/School description'
            }),
            'period' : forms.TextInput(attrs = {
                'placeholder' : 'Duration'
            })
        }
