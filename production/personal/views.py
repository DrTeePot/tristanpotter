from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from tristanpotter.settings import STATIC_PATH
# Create your views here.


def index(request):
    return render(request,
                  'personal/index.html',
        {})


def involvements(request):
    return render(request,
                  'personal/involvements.html',
        {})


def projects(request):
    return render(request,
                  'personal/projects.html',
        {})