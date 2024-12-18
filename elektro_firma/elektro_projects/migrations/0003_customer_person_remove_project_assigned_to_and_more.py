# Generated by Django 5.1.3 on 2024-11-25 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elektro_projects', '0002_remove_project_end_date_remove_project_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.AlterField(
            model_name='project',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='project',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='elektro_projects.customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='assigned_persons',
            field=models.ManyToManyField(related_name='projects', to='elektro_projects.person'),
        ),
    ]
