# Generated by Django 4.0.5 on 2022-07-11 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_remove_profile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
