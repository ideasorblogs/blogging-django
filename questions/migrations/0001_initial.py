# Generated by Django 4.0.5 on 2022-06-28 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0006_alter_blog_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('questions', models.TextField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
        ),
    ]