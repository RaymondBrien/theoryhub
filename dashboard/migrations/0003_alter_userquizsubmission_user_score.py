# Generated by Django 4.2.13 on 2024-07-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_userquizscore_userquizsubmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquizsubmission',
            name='user_score',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
