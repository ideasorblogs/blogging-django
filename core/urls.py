from django.urls import path, include
from . import views
from .views import ProfileView
from .views import *
urlpatterns = [
    path('', TemplateView.as_view(), name="index"),
    path('username/<slug:slug>', ProfileView.as_view(), name="profile"),
]