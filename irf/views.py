from django.shortcuts import render
from resume.models import Job


def workshop(request):
    alljobs = Job.objects.all()

    template = 'irf/workshop.html'
    context = {'alljobs': alljobs}
    return render(request, template, context)