from django.urls import path
from . import views

urlpatterns = [
    path('', views.listview.as_view(), name="blogs"),
    path('add-blog', views.addblog.as_view(), name="add_blog"),
    path('details/<slug:slug>', views.details.as_view(), name="details"),
    path('tags/<slug:slug>/',views.Tags.as_view(), name="btags"),
]
