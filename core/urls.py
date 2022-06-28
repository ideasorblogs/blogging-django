from django.urls import path, include
from . import views
from .views import ProfileView
from .views import *
urlpatterns = [
    path('', views.indexview.as_view(), name="index"),
    path('username/<slug:slug>', ProfileView.as_view(), name="profile"),
    path('add-question/', views.addquestion.as_view(), name="add_question"),
]