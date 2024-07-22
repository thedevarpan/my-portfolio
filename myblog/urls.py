from django.urls import path
from.import views

urlpatterns = [
    path("", views.BlogPost, name = "BlogPost"),
    path("blog-details/<slug:slug>", views.BlogDetails, name = "BlogDetails"),
    path("add-comment/", views.AddComment, name="AddComment"),
] 
