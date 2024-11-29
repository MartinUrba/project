from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    customer = models.CharField(max_length=255)
    assigned_to = models.ManyToManyField('auth.User', related_name='projects')

    def __str__(self):
        return self.name
