# Generated by Django 4.2.13 on 2024-07-18 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_alter_quiz_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=200, unique=True),
        ),
    ]
