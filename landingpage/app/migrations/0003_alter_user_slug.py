# Generated by Django 4.2.15 on 2024-08-27 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
