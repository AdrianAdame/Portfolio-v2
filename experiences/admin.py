from django.contrib import admin

# Register your models here.
from .models import Tech, Experience

admin.site.register(Tech)
admin.site.register(Experience)