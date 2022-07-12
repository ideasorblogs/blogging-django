from django.urls import path, include
from . import views
from .views import *
urlpatterns = [
    path('', views.indexview.as_view(), name="index"),
    path('add-question/', views.addquestion.as_view(), name="add_question"),
]