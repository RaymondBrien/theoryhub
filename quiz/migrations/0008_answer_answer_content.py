# Generated by Django 4.2.13 on 2024-07-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_alter_answer_options_answer_answer_option_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_content',
            field=models.TextField(default='Put multiple-choice answer here'),
        ),
    ]