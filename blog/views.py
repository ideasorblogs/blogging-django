from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from htmlmin.decorators import minified_response

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