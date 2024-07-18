# jobPortalApp/models.py

from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    qualifications = models.TextField()
    contact_info = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields as needed

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
