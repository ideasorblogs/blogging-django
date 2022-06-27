from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from .models import *
from .forms import *
from htmlmin.decorators import minified_response

# Create your views here.

@minified_response
def core(request):
    return render(request, 'index/index.html')



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
    if request.methpd == "POST":
        subscibe = NewsletterForm(request.POST)
        if subscibe.is_valid():
            name = subscibe.cleaned_data['name']
            email = subscibe.cleaned_data['email']
            subscibe.save()
    else:
        return redirect('/')
