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


    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        while question.objects.filter(slug=unique_slug).exists():
            lower_case = string.ascii_lowercase
            upper_case = string.ascii_uppercase
            number = string.digits
            generate = lower_case + upper_case + number
            pass_length = 4
            password_gen = "".join(random.sample(generate, pass_length))
            unique_slug = '{}-{}'.format(slug, password_gen)
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
            super().save(*args, **kwargs)
        else:
            self.slug = slugify(self.title)
            super(question, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quesdetail', args=[self.slug])

