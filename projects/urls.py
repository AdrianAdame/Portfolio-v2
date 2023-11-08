from django.urls import path
from .views import projects, project_new

urlpatterns = [
    path("", projects, name="projects"),
    path("new/", project_new, name = "project_new")
]