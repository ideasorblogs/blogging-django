# Generated by Django 4.0.5 on 2022-07-06 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0024_alter_question_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='time',
        ),
    ]
