# Generated by Django 4.0.5 on 2022-06-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_remove_question_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]