# Generated by Django 4.0.5 on 2022-06-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_alter_question_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(auto_created=True, max_length=200, unique=True),
        ),
    ]
