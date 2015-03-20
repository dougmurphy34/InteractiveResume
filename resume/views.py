from django.shortcuts import render
from django.http import HttpResponse
from resume.models import Job


def index(request):
    return HttpResponse("First page of the final app")


def allmyjobs(request):
    jobs = Job.objects.get_queryset()

    return render(request, 'resume/joblist.html', {'joblist': jobs})
