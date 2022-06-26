from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def questions(request):
    return render(request, 'questions/questions.html')