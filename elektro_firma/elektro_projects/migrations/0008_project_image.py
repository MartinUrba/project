# Generated by Django 5.1.3 on 2024-11-30 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elektro_projects', '0007_remove_project_assigned_persons_remove_project_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='default_project_image.jpg', upload_to='project_images/'),
        ),
    ]