from django.urls import path, include
from . import views
from .views import ProfileView
from .views import *
urlpatterns = [
    path('', views.core, name="index"),
    path('newsletter', views.newsletter, name="newsletter"),
    path('username/<slug:slug>', ProfileView.as_view(), name="profile"),
]