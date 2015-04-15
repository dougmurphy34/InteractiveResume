from django.shortcuts import render
from django.http import HttpResponse
from resume.models import Job

'''
nbar is passed in context to tell the Boostrap Navigation bar in base.py which menu item should be highlighted as "active"
'''


def index(request):
    template = 'irf/welcome.html'
    context = {'nbar': "index"}
    return render(request, template, context)


def all_my_jobs(request):
    jobs = Job.objects.get_queryset().order_by('start_date')
    if len(jobs) == 0:
        template = 'irf/error.html'
        context = {'error_text': 'No jobs found in database'}
    else:
        template = 'resume/job_list.html'
        context = {'joblist': jobs, 'nbar': "all_my_jobs"}

    return render(request, template, context)


def job_detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        template = 'resume/job_detail.html'
        context = {'job': job, 'nbar': "job_detail"}
    except:
        template = 'irf/error.html'
        context = {'error_text': "That job doesn't seem to exist."}

    return render(request, template, context)


def contact(request):
    template = 'irf/contact.html'
    context = {'nbar': "contact"}

    return render(request, template, context)


def portfolio(request):
    template = 'resume/portfolio.html'
    context = {'nbar': "portfolio"}

    return render(request, template, context)


def resume(request):
    template = 'resume/resume.html'
    jobs = Job.objects.get_queryset().order_by('start_date')
    context = {'joblist': jobs, 'nbar': "resume"}

    return render(request, template, context)


