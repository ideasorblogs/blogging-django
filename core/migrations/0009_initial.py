# Generated by Django 4.0.5 on 2022-06-27 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0008_delete_employe_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
