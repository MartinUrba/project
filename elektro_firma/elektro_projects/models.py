from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    assigned_to = models.CharField(max_length=100)  # osoba přiřazená k projektu


    def __str__(self):
        return self.name
