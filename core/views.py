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


def get_started(request):
    return render(request, 'user/get_started.html')


class ProfileView(LoginRequiredMixin, View):
    @minified_response
    def get(self, request,*args, **kwargs):
        details = employe_details.objects.filter(employee=request.user)
        context = {
            'details': details
        }
        return render(request, 'user/profile.html', context)

@minified_response
def edit(request, pk):
    details = employe_details.objects.get(pk=pk)
    form = edit_profile_form(request.POST or None, instance=details)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'user/edit-profile.html', {'form':form, 'details':details})