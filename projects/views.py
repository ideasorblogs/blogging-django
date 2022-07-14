from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from hitcount.views import HitCountDetailView

from .models import *
# Create your views here.
from django.views.generic import *


class project(ListView):
    model = projects
    template_name = 'projects/projects.html'
    paginate_by = 10

class Tags(ListView):
    model = question
    template_name = 'projects/projects.html'
    context_object_name = 'tags'
    paginate_by = 10

    def get_queryset(self):
        return projects.objects.filter(tags__slug=self.kwargs.get('slug'))

class project_details(HitCountDetailView):
    model = projects
    template_name = 'projects/projects_details.html'
    count_hit = True