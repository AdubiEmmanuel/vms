from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=200, default=False)
    address = models.CharField(max_length=100, default=False)
    country = models.CharField(max_length=500)
    nationality = models.CharField(max_length=500)
#     Name 
# Email 
# Phone number 
# Address 
# Country 
# Nationality 


# Register fields 
# Client 
# Name 
# Email 
# Password 
# Re enter password 

# Vendors
# Company name 
# Address
# City
# Country 
# Phone number 
# Password
# Re enter password
