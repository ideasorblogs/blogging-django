from django.contrib import admin
from .models import *

# Register your models here.

class qadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}
    list_display = ['title', 'author', 'created_on']

admin.site.register(question, qadmin)
