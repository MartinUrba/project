from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    assigned_to = models.ManyToManyField(User, related_name='projects')
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)  # Pole pro obrázek

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # URL na detail projektu
        return reverse('project-detail', kwargs={'pk': self.pk})

