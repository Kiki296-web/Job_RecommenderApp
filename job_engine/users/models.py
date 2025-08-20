from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # add custom fields here
    skills = models.TextField(blank=True, null=True)
    preferred_job = models.CharField(max_length=100, blank=True, null=True)
    preferred_location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username


