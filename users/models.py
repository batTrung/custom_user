# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	address= models.CharField(max_length=100, null=True, blank=True)
