# jobPortalApp/admin.py

from django.contrib import admin
from .models import Job, UserProfile

admin.site.register(Job)
admin.site.register(UserProfile)
