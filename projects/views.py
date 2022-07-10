from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import *


def projects(request):
    return render(request, 'projects/projects.html')

