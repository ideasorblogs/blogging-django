from django.contrib import admin
from .models import *
# Register your models here.

class projectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['title', 'author', 'created_on']

admin.site.register(projects, projectAdmin)