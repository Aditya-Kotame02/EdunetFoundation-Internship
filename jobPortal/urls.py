"""
URL configuration for jobPortal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from jobPortalApp import views

urlpatterns = [
    path('', views.index, name='index'),  # Maps the root URL to the index view
    path('candidate-dashboard/', views.candidate_dashboard, name='candidate_dashboard'),
    path('hr-dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('admin/', admin.site.urls),
    path('add_job/', views.add_job, name='add_job'),
    path('apply-job/<int:job_id>/', views.apply_job, name='apply_job'),
    # Add other URL patterns as needed
]
