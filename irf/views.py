from django.shortcuts import render
from resume.models import Job


def workshop(request):
    alljobs = Job.objects.all()

    template = 'irf/workshop.html'
    context = {'alljobs': alljobs}
    return render(request, template, context)

def workshop2(request):
    template = 'irf/workshop2.html'
    context = {}
    return render(request, template, context)