# Generated by Django 4.0.5 on 2022-07-26 08:36

from django.db import migrations, models
import projects.validators


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_projects_uploaded_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='uploaded_file',
            field=models.FileField(upload_to='projects/uploads/%Y/%m/%d', validators=[projects.validators.validate_file_extension]),
        ),
    ]
