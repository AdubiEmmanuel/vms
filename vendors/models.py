from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    type_of_software = models.CharField(max_length=200, default=False)
    contact_telephone_no = models.CharField(max_length=200, default=False)
    vendor_id = models.PositiveIntegerField()
    website = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default=False)
    software_name = models.CharField(max_length=50)
    company_established = models.PositiveIntegerField(default=False)
    no_of_employees = models.PositiveIntegerField(default=False)
    location_countries = models.CharField(max_length=500)
    location_cities = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default=False)
    internal_professional_services = models.CharField(max_length=3, default=False)
    last_demo_date = models.CharField(max_length=20, default=False)
    last_reviewed_date = models.CharField(max_length=20)
    business_areas = models.CharField(max_length=200, default=False)
    modules = models.CharField(max_length=50)
    financial_services_client_types = models.CharField(max_length=100, default=False)
    cloud_options = (
        ('cloud_native', 'cloud_native'),
        ('cloud_based', 'cloud_based'),
        ('cloud_enabled', 'cloud_enabled'),
    )
    cloud_type=models.CharField(
        max_length=200,
        choices=cloud_options,
        blank=True,
        null=True
    )
    additional_info = models.CharField(max_length=500, default=False)
    document_to_attach = models.CharField(max_length=3, default=False)
    
    
    def __str__(self):
        return self.user.username 
