from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.training, name="trainings"),
]