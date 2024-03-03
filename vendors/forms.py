from django import forms
from django.contrib.auth.models import User 
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.forms import  UserCreationForm
from .models import Vendor 

class VendorForm(UserCreationForm):
    company_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    type_of_software = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_telephone_no = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    vendor_id = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    product_category = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    software_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    company_established = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    no_of_employees = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location_countries = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location_cities = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    internal_professional_services = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_demo_date = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    business_areas = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    modules = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    financial_services_client_types = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cloud_options = (
        ('select_cloud_type', 'select_cloud_type'),
        ('cloud_native', 'cloud_native'),
        ('cloud_based', 'cloud_based'),
        ('cloud_enabled', 'cloud_enabled'),
    )
    cloud_type = forms.ChoiceField(label='', choices=cloud_options, widget=forms.Select(attrs={'class':'form-control'}))
    additional_info = forms.CharField(required=False, max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    document_to_attach = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            client = Vendor.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                address=self.cleaned_data['address'],
                country=self.cleaned_data['country'],
                nationality=self.cleaned_data['nationality']
            )
        return user


        