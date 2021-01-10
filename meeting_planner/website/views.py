from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner")


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about_me(request):
    return HttpResponse("I am will. I am writing a silly about me page"
                        "Python seems to be pretty cool. Much smaller than"
                        "Java.  Linebreaks?")