# Generated by Django 4.2.13 on 2024-07-25 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_quiznote'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userquizsubmission',
            options={'ordering': ['-last_taken']},
        ),
    ]
