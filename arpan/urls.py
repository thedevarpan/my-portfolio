from django.urls import path
from.import views

urlpatterns = [
    path("", views.Index, name = "Index"),
    path("project-details/", views.ProjectDetails, name = "ProjectDetails"),
] 
