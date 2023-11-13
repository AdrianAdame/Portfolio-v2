from django.urls import path
from .views import experiences, experience_new


urlpatterns =[
    path("", experiences, name = "experiences"),
    path("new/", experience_new, name = "experience_new")
]