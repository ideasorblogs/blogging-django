from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from hitcount.views import HitCountDetailView
from htmlmin.decorators import minified_response

from .models import *
from blog.models import *
# Create your views here.
from questions.forms import *

class QuestionListview(ListView):
    model = question
    template_name = 'questions/questions.html'
    context_object_name = 'count'
    ordering = '-created_on', '-time'
    paginate_by = 12



def count(request):
    count = question.objects.all().count()
    context = {
        'count':count
    }
    return render(request, 'questions/questions.html', context)


def search(request):
    quest = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        quest = question.objects.all().filter(Q(title__icontains=query) | Q(questions__icontains=query))

    return render(request, 'questions/question_search.html', {'qu': query, 'qr': quest})

class Tags(ListView):
    model = question
    template_name = 'questions/questions.html'
    context_object_name = 'tags'
    paginate_by = 10

    def get_queryset(self):
        return question.objects.filter(tags__slug=self.kwargs.get('slug'))

class questiondetail(HitCountDetailView, DeleteView):
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






