from django.shortcuts import render
from django.http import HttpResponse
from resume.models import Job, Skill

'''
nbar is passed in context to tell the Boostrap Navigation bar in base.py which menu item
    should be highlighted as "active"
'''


def index(request):
    template = 'irf/welcome.html'
    context = {'nbar': "index"}
    return render(request, template, context)


def all_my_jobs(request):  # doesn't match template name, should probably rename this view
    jobs = Job.objects.get_queryset().order_by('-start_date')
    skills = Skill.objects.all().exclude(skill_logo__exact=None)

    if len(jobs) == 0:
        template = 'irf/error.html'
        context = {'error_text': 'No jobs found in database'}
    elif len(skills) == 0:
        template = 'irf/error.html'
        context = {'error_text': 'No skills found in database'}
    else:
        template = 'resume/job_list.html'
        context = {'joblist': jobs, 'skilllist': skills, 'nbar': "all_my_jobs"}

    return render(request, template, context)

# replace this with job_detail_all
def job_detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        template = 'resume/job_detail.html'
        context = {'job': job, 'nbar': "job_detail"}
    except:
        template = 'irf/error.html'
        context = {'error_text': "That job doesn't seem to exist."}

    return render(request, template, context)

# Use this instead of job_detail, when implementing tab-based job detail view
def job_detail_all(request, job_id):
    try:
        jobs = Job.objects.all().order_by('start_date')
        job_id_selected = int(job_id)
        template = 'resume/job_detail.html'
        context = {'jobs': jobs, 'job_id_selected': job_id_selected, 'nbar': "job_detail"}

    except:
        template = 'irf/error.html'
        context = {'error_text': "Loading all the jobs went poorly."}
    return render(request, template, context)


def contact(request):
    template = 'irf/contact.html'
    context = {'nbar': "about"}

    return render(request, template, context)


def portfolio(request):
    template = 'resume/philosophy.html'

    context = {'nbar': "portfolio"}

    return render(request, template, context)
