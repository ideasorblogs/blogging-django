from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:slug>/', views.ProfileView.as_view(), name="profile"),
]