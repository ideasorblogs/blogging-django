from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import *
from .forms import *
from htmlmin.decorators import minified_response

# Create your views here.

@minified_response
class DashboardView(View):
    template_name = "index/index.html"

    def newsletter(self, request):
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            s = newsletter(name=name, email=email)
            s.save()
            messages.success(request, "subscribed successfully")



class ProfileView(LoginRequiredMixin, View):
    @minified_response
    def get(self, request,*args, **kwargs):
        details = employe_details.objects.filter(employee=request.user)
        context = {
            'details': details
        }
        return render(request, 'user/profile.html', context)

@minified_response
def newsletter(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        s = newsletter(name=name, email=email)
        s.save()
        messages.success(request, "subscribed successfully")
    return render(request, 'index/newsletter.html')
