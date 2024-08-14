# Generated by Django 4.2.15 on 2024-08-14 08:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0004_author_full_name_author_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
    ]
