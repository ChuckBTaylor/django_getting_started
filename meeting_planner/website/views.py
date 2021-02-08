from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html", {"num_meetings": Meeting.objects.count()})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about_me(request):
    return HttpResponse("I am will. I am writing a silly about me page"
                        "Python seems to be pretty cool. Much smaller than"
                        "Java.  Linebreaks?")