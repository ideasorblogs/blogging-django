# Generated by Django 4.0.5 on 2022-06-30 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_delete_questionviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='search',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
