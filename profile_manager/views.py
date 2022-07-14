from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from htmlmin.decorators import minified_response
from questions.models import *

class ProfileView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'profile_manager/profile.html'
    @minified_response
    def get(self, request,*args, **kwargs):
        details = User.objects.filter(id=request.user.id)
        context = {
            'details': details,
        }
        return render(request, 'profile_manager/profile.html', context)

class My_Questions(ListView):
    model = question
    template_name = 'profile_manager/profile_questions.html'
    context_object_name = 'que'

    def get(self, request, *args, **kwargs):
        que = question.objects.filter(author=request.user).order_by('-time')
        context = {
            'que':que,
        }
        return render(request, 'profile_manager/profile_questions.html', context)

class Tags(ListView):
    model = question
    template_name = 'profile_manager/profile_questions.html'
    context_object_name = 'tags'
    def get_queryset(self):
        return question.objects.filter(tags__slug=self.kwargs.get('slug'))
