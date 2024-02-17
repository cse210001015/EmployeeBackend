from django.urls import path
from . import views


urlpatterns = [
    path("<int:employeeId>", views.manageEmployee.as_view()),
    path("", views.manageEmployees.as_view()),
]