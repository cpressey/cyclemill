from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>It works!</h1>", content_type="text/html")
