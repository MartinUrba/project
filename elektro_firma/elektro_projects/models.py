from django.db import models
from django.urls import reverse



class Project(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    assigned_to = models.ManyToManyField('people.Person', related_name='projects')  # Zde vložte upravený řádek
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})