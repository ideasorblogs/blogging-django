from django.urls import path, include
from . import views
from .views import ProfileView
from .views import *
urlpatterns = [
    path('', views.core, name="index"),
    path('get-started/', views.get_started, name="get_started"),
    path('username/<slug:slug>', ProfileView.as_view(), name="profile"),
    path('edit-details/<int:pk>',edit , name="edit_details")
]