# Generated by Django 4.2.13 on 2024-07-16 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_quiz_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
