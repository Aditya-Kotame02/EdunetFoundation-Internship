from django.shortcuts import render, redirect
from .forms import JobForm
from django.http import HttpResponse
from .models import Job


def index(request):
    return render(request, 'index.html')

def candidate_dashboard(request):
    return render(request, 'candidate-dashboard.html')

def hr_dashboard(request):
    return render(request, 'hr-dashboard.html')


def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hr_dashboard')  # Redirect to HR Dashboard after adding job
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})

def candidate_dashboard(request):
    jobs = Job.objects.all()
    return render(request, 'candidate_dashboard.html', {'jobs': jobs})


def apply_job(request, job_id):
    # Retrieve the job object
    try:
        job = Job.objects.get(pk=job_id)
    except Job.DoesNotExist:
        return HttpResponse('Job not found', status=404)

    # Implement your logic for job application here

    return redirect('candidate_dashboard')  # Redirect back to the candidate dashboard after applying
