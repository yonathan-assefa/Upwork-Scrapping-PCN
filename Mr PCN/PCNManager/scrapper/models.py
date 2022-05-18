import email
from pyexpat import model
from django.db import models


class PCN(models.Model):
    pcn = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.TextField()
    location = models.CharField(max_length=255)
    control_number = models.CharField(max_length=30)
    subdivision = models.CharField(max_length=255)
    legal_description = models.TextField()

    def __str__(self):
        return self.pcn

class directory(models.Model):
    fname = models.CharField(max_length=500)
    lname = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    email_old = models.CharField(max_length=500)
    phone1 = models.CharField(max_length=500)    
    phone1_old = models.CharField(max_length=500)    
    phone2 = models.CharField(max_length=500)    
    phone2_old = models.CharField(max_length=500)    
    address = models.CharField(max_length=500)    
    city = models.CharField(max_length=500)    
    state = models.CharField(max_length=500)    
    zip = models.CharField(max_length=500)    
    community = models.CharField(max_length=500)    

    def __str__(self):
        return self.fname
