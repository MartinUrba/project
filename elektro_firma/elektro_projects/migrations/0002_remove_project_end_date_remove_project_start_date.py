# Generated by Django 5.1.3 on 2024-11-17 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elektro_projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
    ]
