# Generated by Django 4.2.13 on 2024-07-09 08:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_quiz_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(50)]),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(10)]),
        ),
    ]
