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
        
    # def __init__(self, *args, **kwargs):
    #     super.__init__(*args, **kwargs)
    #     self.fields('name').widget.attrs.update({'class': 'form-control'})
            
        
