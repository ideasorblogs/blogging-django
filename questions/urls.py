from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.QuestionListview.as_view(), name="questions"),
    path('details/<slug:slug>', views.questiondetail.as_view(), name="quesdetail"),
    path('edit/<slug:slug>', views.questionupdate.as_view(), name="quesupdate"),
    path('delete/<slug:slug>', views.questionupdate.as_view(), name="quesdelete"),
    path('search/', views.search, name="search"),
]