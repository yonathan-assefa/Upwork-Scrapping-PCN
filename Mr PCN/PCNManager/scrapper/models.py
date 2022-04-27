import email
from pyexpat import model
from django.db import models


class PCN(models.Model):
    pcn = models.CharField(max_length=14)
    owner = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255)
    control_number = models.CharField(max_length=30)
    subdivision = models.CharField(max_length=255)
    legal_description = models.TextField()

    def __str__(self):
        return self.pcn