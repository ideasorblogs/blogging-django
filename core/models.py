from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class employe_details(models.Model):
    employee = models.ForeignKey(User,primary_key=True ,verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    about = models.TextField(max_length=1000, blank=True, null=True)
    skills = TaggableManager()
    experience = models.DateField()
    education = models.TextField(max_length=1000, blank=True, null=True)
    added_on = models.DateTimeField()
