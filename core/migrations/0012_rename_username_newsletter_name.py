# Generated by Django 4.0.5 on 2022-06-27 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_name_newsletter_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='username',
            new_name='name',
        ),
    ]
