from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.LoginManager.as_view()),
    path("<int:userId>", views.userManager.as_view()),
    path("", views.usersManager.as_view()),
]