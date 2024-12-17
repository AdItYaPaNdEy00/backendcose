from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    skills = models.TextField(null=True, blank=True)
    interests = models.TextField(null=True, blank=True)