from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from htmlmin.decorators import minified_response


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
