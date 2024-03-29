from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default=False)
    location_countries = models.CharField(max_length=500)
    
    def __str__(self):
        return self.user.username 
