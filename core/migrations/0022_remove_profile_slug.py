# Generated by Django 4.0.5 on 2022-07-11 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]
