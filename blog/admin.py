from django.contrib import admin
from .models import *
# Register your models here.

class Blogadmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_on', 'is_active']
    list_editable = ['is_active']
    prepopulated_fields = {'slug':['title']}

class categorieadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}

admin.site.register(blog, Blogadmin)
admin.site.register(category, categorieadmin)