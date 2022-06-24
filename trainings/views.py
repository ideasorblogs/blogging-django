from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def training(request):
    return render(request, 'trainings/trainings.html')