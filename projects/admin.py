from django.contrib import admin

# Register your models here.
from .models import Tech, Project

admin.site.register(Project)
admin.site.register(Tech)