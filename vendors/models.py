from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    company_address = models.TextField()
    phone_number = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.user.username 
