from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def events(request):
    return render(request, 'events/event.html')