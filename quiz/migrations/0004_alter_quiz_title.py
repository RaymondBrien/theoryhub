# Generated by Django 4.2.13 on 2024-07-09 09:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_quiz_description_alter_quiz_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(20)]),
        ),
    ]
