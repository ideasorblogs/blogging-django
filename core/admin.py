from django.contrib import admin
# Register your models here.

from .models import *

class Newsletter(admin.ModelAdmin):
    list_display = ['name', 'email','subscribed_on']

admin.site.register(newsletter, Newsletter)


