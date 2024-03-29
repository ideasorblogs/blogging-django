# Generated by Django 4.0.5 on 2022-06-10 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_rename_update_on_employe_details_added_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe_details',
            name='employee',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='employee'),
        ),
    ]
