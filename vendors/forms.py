from django import forms
from .models import Vendor
from django.contrib.auth.models import User 



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        
        
class VendorCreateForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        
