from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from htmlmin.decorators import minified_response

from .models import *
from blog.models import *
# Create your views here.
from questions.forms import *

@minified_response
def questions(request):
    qu = question.objects.all().order_by('-time').values()
    context = {
        'question':qu
    }
    return render(request, 'questions/questions.html', context)

class questiondetail(DetailView, DeleteView):
    model = question
    template_name = "questions/question_details.html"
    success_url = reverse_lazy('questions')


class questionupdate(UpdateView):
    model = question
    template_name = "questions/update_question.html"
    fields = ['title', 'questions', 'categorie']
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

class questiondelete(DeleteView):
    model = question
    template_name = "questions/question_details.html"
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    success_url = reverse_lazy('questions')






