from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from htmlmin.decorators import minified_response
from .forms import *
from .models import *

@minified_response
def blogs(request):
    dis = blog.objects.all().order_by('-time')
    context = {
        'display':dis
    }
    return render(request, 'blogs/blogs.html', context)

class details(DetailView):
    model = blog
    template_name = "blogs/blog_detail.html"
    slug_url_kwarg = 'slug'
    slug_field = 'slug'


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