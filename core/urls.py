from django.urls import path, include
from . import views
from .views import ProfileView
from .views import *
urlpatterns = [
    path('', views.indexview.as_view(), name="index"),
    path('bookmarks/', views.bookmarks, name="bookmarks"),
    path('profile/<slug:slug>', ProfileView.as_view(), name="profile"),
    path('add-question/', views.addquestion.as_view(), name="add_question"),
    path('profile/<slug:slug>/questions/', views.my_questions.as_view(), name="my_questions"),
    path('profile/<slug:slug>/answers/', views.my_answers.as_view(), name="my_answers"),
    path('profile/<slug:slug>/friends/', views.my_friends.as_view(), name="my_friends"),
    path('profile/<slug:slug>/blogs/', views.my_blogs.as_view(), name="my_blogs"),
    path('profile/<slug:slug>/bookmarks/', views.my_bookmarks.as_view(), name="my_bookmarks"),
    path('profile/<slug:slug>/downloads/', views.my_downloads.as_view(), name="my_downloads"),
    path('profile/<slug:slug>/email-settings/', views.email_settings.as_view(), name="email_settings"),
    path('profile/<slug:slug>/account-settings/', views.account_settings.as_view(), name="account_settings"),
]