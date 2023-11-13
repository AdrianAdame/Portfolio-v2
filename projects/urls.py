from django.urls import path
from .views import projects, project_new

# For image usage
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", projects, name="projects"),
    path("new/", project_new, name = "project_new")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)