from django.shortcuts import render

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


def about(request):
    return render(request,
                  'personal/about.html',
                  {})