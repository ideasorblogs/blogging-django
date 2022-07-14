from django.urls import path, include
from . import views
from .views import *
urlpatterns = [
    path('', views.project.as_view(), name="projects"),
    path('details/<slug:slug>/', views.project_details.as_view(), name="projectdetails")
]