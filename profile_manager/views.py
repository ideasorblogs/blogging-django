from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from htmlmin.decorators import minified_response
from questions.models import *
from blog.models import *

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

    def cou(self, request):
        q_count = question.objects.filter(author=request.user).count()
        context = {
            'q_count':q_count
        }
        return render(request, 'profile_manager/profile_questions.html', context)


class Tags(ListView):
    model = question
    template_name = 'profile_manager/profile_questions.html'
    context_object_name = 'tags'
    def get_queryset(self):
        return question.objects.filter(tags__slug=self.kwargs.get('slug'))

class My_blogs(ListView):
    model = blog
    template_name = 'profile_manager/profile_blogs.html'
    context_object_name = 'blo'
    def get(self, request, *args, **kwargs):
        blo = blog.objects.filter(author=request.user).order_by('-time')
        context = {
            'blo':blo
        }
        return render(request, 'profile_manager/profile_blogs.html', context)

class My_bookmarks(ListView):
    model = blog
    template_name = 'profile_manager/profile_bookmarks.html'
    context_object_name = 'book_mark'
    def get(self, request, *args, **kwargs):
        book = blog.objects.filter(bookmarks=request.user).order_by('-time')
        context = {
            'book':book
        }
        return render(request, 'profile_manager/profile_bookmarks.html', context)
