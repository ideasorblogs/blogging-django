
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField()
    article = models.TextField()

class category(models.Model):
    name = models.TextField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)