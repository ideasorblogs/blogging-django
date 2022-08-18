from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug:slug>/', views.ProfileView.as_view(), name="profile"),
    path('<slug:slug>/questions/', views.My_Questions.as_view(), name="my_questions"),
    path('<slug:slug>/blogs', views.My_blogs.as_view(), name="my_blogs"),
    path('<slug:slug>/bookmarks', views.My_bookmarks.as_view(), name="my_bookmarks")
]