from django.shortcuts import render
from django.http import HttpResponse
from resume.models import Job


def index(request):
    template = 'irf/welcome.html'
    context = ''
    return render(request, template, context)


def allmyjobs(request):
    jobs = Job.objects.get_queryset().order_by('start_date')

    return render(request, 'resume/joblist.html', {'joblist': jobs})
