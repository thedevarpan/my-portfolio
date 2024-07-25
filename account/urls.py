from django.urls import path
from.import views

urlpatterns = [
    path("", views.Account, name="Account"),
    path("signup/", views.Signup, name="Signup"),
    path("login/", views.Login, name="Login"),
    path("profile/", views.Profile, name="Profile"),
] 