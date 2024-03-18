from django import forms
from django.contrib.auth.models import User 
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.forms import  UserCreationForm
from .models import Product 

cloud_options = (
        ('select_cloud_type', 'select_cloud_type'),
        ('cloud_native', 'cloud_native'),
        ('cloud_based', 'cloud_based'),
        ('cloud_enabled', 'cloud_enabled'),
    )

class ProductForm(UserCreationForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
                    'company_name':forms.TextInput(attrs={'class': 'form-control'}),
                    'type_of_software' :forms.TextInput(attrs={'class': 'form-control'}),
                    'contact_telephone_no':forms.TextInput(attrs={'class': 'form-control'}),
                    'vendor_id':forms.TextInput(attrs={'class': 'form-control'}),
                    'website': forms.TextInput(attrs={'class': 'form-control'}),
                    'product_category':forms.TextInput(attrs={'class': 'form-control'}),
                    'description':forms.TextInput(attrs={'class': 'form-control'}),
                    'company_established':forms.TextInput(attrs={'class': 'form-control'}),
                    'no_of_employees':forms.TextInput(attrs={'class': 'form-control'}),
                    'location_countries':forms.TextInput(attrs={'class': 'form-control'}),
                    'internal_professional_services':forms.TextInput(attrs={'class': 'form-control'}),
                    'last_demo_date':forms.TextInput(attrs={'class': 'form-control'}),
                    'business_areas':forms.TextInput(attrs={'class': 'form-control'}),
                    'modules':forms.TextInput(attrs={'class': 'form-control'}),
                    'financial_services_client_types': forms.TextInput(attrs={'class': 'form-control'}),
                    'additional_info':forms.TextInput(attrs={'class': 'form-control'}),
                    'cloud_type' :forms.ChoiceField(choices=cloud_options, widget=forms.Select(attrs={'class':'form-control'})),
                    'document_to_attach':forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
        }
                    
                

    

        