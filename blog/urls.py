from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('details/<slug:slug>', views.details.as_view(), name="details")
]
