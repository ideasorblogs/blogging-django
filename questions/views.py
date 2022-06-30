from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from htmlmin.decorators import minified_response

from .models import *
from blog.models import *
# Create your views here.
from questions.forms import *

class QuestionListview(ListView):
    model = question
    template_name = 'questions/questions.html'
    context_object_name = 'count'
    def count(self, request):
        count = question.objects.count()
        return render(request, 'questions/questions.html', count)

class questiondetail(DetailView, DeleteView):
    model = question
    template_name = "questions/question_details.html"
    success_url = reverse_lazy('questions')
    count_hit = True


class questionupdate(UpdateView):
    model = question
    form_class = UpdateForm
    template_name = "questions/update_question.html"
    slug_url_kwarg = 'slug'
    slug_field = 'slug'


class questiondelete(DeleteView):
    model = question
    template_name = "questions/update_question.html"
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    success_url = reverse_lazy('questions')






