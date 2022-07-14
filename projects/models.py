import random
import string

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from hitcount.models import HitCount
from django.utils.text import slugify
from questions.models import *
from taggit.managers import TaggableManager

from .validators import validate_file_extension

# Create your models here.

class projects(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, auto_created=True)
    details = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='projects/images')
    uploaded_file = models.FileField('documents/%Y/%m/%d', validators=[validate_file_extension])
    created_on = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )

    def current_hit_count(self):
        return self.hit_count.hits

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        while projects.objects.filter(slug=unique_slug).exists():
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
            super(projects, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projectdetails', args=[self.slug])
