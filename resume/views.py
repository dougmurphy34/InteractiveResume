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
    context = {'nbar': "about"}

    return render(request, template, context)


def portfolio(request):
    template = 'resume/portfolio.html'

    # This try/except is needed because the unit test on the view has no HTTP_USER_AGENT and throws an exception
    # This seems like a dumb answer (should I write a fake one in the test to handle this?)
    try:
        useragentstring = request.META['HTTP_USER_AGENT']
    except:
        useragentstring = ''

    context = {'nbar': "portfolio", 'browser': useragentstring}

    return render(request, template, context)

