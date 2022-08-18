from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from hitcount.views import HitCountDetailView
from htmlmin.decorators import minified_response
from .forms import *
from .models import *

class listview(ListView):
    model = blog
    template_name = "blogs/blogs.html"
    ordering = '-time'
    context_object_name = 'blogs'


class details(HitCountDetailView):
    model = blog
    template_name = "blogs/blog_detail.html"
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    context_object_name = 'blogdetails'
    count_hit = True



class Tags(ListView):
    model = blog
    template_name = 'blogs/blogs.html'
    context_object_name = 'tags'
    paginate_by = 10

    def get_queryset(self):
        return blog.objects.filter(tags__slug=self.kwargs.get('slug'))


class addblog(LoginRequiredMixin,CreateView):
    model = blog
    form_class = BlogForm
    template_name = 'blogs/add_blog.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class blogupdate(UpdateView):
    model = blog
    template_name = 'blogs/blog_update.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'