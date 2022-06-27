from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
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
            messages.success(request, "Subscribed successfully")
            subject = 'NewsLetter Subscription'
            message = 'Hello , Thanks for subscribing us. You will get notification of latest articles posted on our website. Please do not reply on this email.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [form.email, ]
            send_mail(subject, message, email_from, recipient_list)
        else:
            messages.error(request, "Something went wrong")
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

