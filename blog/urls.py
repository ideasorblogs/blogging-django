from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path('add-blog', views.addblog.as_view(), name="add_blog"),
    path('details/<slug:slug>', views.details.as_view(), name="details")
]
