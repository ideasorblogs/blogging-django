# Generated by Django 4.0.5 on 2022-07-01 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_remove_question_categorie_alter_question_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
