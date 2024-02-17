from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(max_length = 200)
    position = models.CharField(max_length = 200)
    department = models.CharField(max_length = 200)
    salary = models.IntegerField()
    age = models.IntegerField()