from django.contrib import messages
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
    form = NewsletterForm()
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            if newsletter.objects.filter(email='email').exists():
                messages.error(request, "Email already exists")

    context = {'form':form}
    return render(request, 'index/index.html', context)



class ProfileView(LoginRequiredMixin, View):
    @minified_response
    def get(self, request,*args, **kwargs):
        details = employe_details.objects.filter(employee=request.user)
        context = {
            'details': details
        }
        return render(request, 'user/profile.html', context)

