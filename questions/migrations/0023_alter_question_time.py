# Generated by Django 4.0.5 on 2022-07-06 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0022_question_updates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
