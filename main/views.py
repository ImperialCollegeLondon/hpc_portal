from itertools import chain

from django.conf import settings
from django.shortcuts import redirect, render

from .forms import SubmissionForm
from .models import Job


def index(request):
    return render(request, "main/index.html")


def create_job(request):
    if request.method == "POST":
        software = settings.SOFTWARE["gaussian16"]
        form = SubmissionForm(request.POST, request.FILES)
        files_spec = software["input_files"]
        if form.is_valid():
            input_files = {
                key: request.FILES[key]
                for key in chain(files_spec["required"], files_spec["optional"])
                if key in request.FILES
            }

            job = Job.objects.create_job(input_files)
            return redirect("main:success", job.pk)
    else:
        form = SubmissionForm()
    return render(request, "main/create_job.html", {"form": form})


def success(request, job_pk):
    job = Job.objects.get(pk=job_pk)
    return render(request, "main/success.html", {"job_id": job.job_id})
