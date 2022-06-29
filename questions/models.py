import random
import uuid
from datetime import time

from django.contrib.auth.models import User
from django.db import models
import string
# Create your models here.
from blog.models import *
from django.urls import reverse
from django.utils.text import slugify


class question(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, auto_created=True)
    categorie = models.ForeignKey(category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    questions = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now=True)

    def save(self, *args, **kwargs):
        lower_case = 'abcedfghijklmnopqrstuvwxyz'
        upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number = '123456789'
        generate = lower_case + upper_case + number
        slug_length = 3
        slug_gen = "".join(random.sample(generate, slug_length))
        string = "%s-%s" % (slug_gen[0:], self.title)
        self.slug = slugify(string)
        super(question, self).save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quesdetail', args=[self.slug])