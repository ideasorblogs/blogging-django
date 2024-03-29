from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.


class newsletter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    subscribed_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


