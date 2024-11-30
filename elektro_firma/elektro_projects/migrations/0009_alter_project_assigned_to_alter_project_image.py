# Generated by Django 5.1.3 on 2024-11-30 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elektro_projects', '0008_project_image'),
        ('people', '0002_rename_name_person_first_name_remove_person_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='assigned_to',
            field=models.ManyToManyField(related_name='projects', to='people.person'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/images/'),
        ),
    ]
