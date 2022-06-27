from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class newsletter(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)