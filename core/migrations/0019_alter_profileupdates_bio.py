# Generated by Django 4.0.5 on 2022-07-11 14:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_profileupdates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileupdates',
            name='bio',
            field=ckeditor.fields.RichTextField(),
        ),
    ]