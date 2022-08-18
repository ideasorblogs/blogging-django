import random
import string

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify
from hitcount.models import HitCount
from taggit.managers import TaggableManager
import readtime


class category(models.Model):
    name = models.CharField(max_length=50, unique=True, default="django")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name
    


class blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='blogs/thumbnail/%Y/%m/%d', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now=True)
    article = RichTextField()
    categorie = models.ForeignKey(category, on_delete=models.CASCADE, null=True, blank=True)
    tags = TaggableManager(blank=True)
    is_active = models.BooleanField(default=False)

    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )

    def current_hit_count(self):
        return self.hit_count.hits

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        while blog.objects.filter(slug=unique_slug).exists():
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
            super(blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', args=[self.slug])

    @property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/banner.png"

    def get_readtime(self):
        result = readtime.of_text(self.article)
        return result.text




