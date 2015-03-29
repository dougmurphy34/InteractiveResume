from django.shortcuts import render
from django.http import HttpResponse
from resume.models import Job


def index(request):
    template = 'irf/welcome.html'
    context = ''
    return render(request, template, context)


def all_my_jobs(request):
    jobs = Job.objects.get_queryset().order_by('start_date')

    return render(request, 'resume/job_list.html', {'joblist': jobs})


def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)

    return render(request, 'resume/job_detail.html', {'job': job})