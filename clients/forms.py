from django import forms
from django.contrib.auth.models import User 
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.forms import  UserCreationForm
from .models import Client 

class ClientForm(UserCreationForm):
    phone_number =forms.CharField(max_length=200)
    address =forms.CharField(max_length=200, widget=TextInput(attrs={'class:': 'form-control'}))
    country =forms.CharField(max_length=200, widget=TextInput(attrs={'class:': 'form-control'}))
    nationality =forms.CharField(max_length=200, widget=TextInput(attrs={'class:': 'form-control'}))
    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'email','phone_number', 'address', 'country', 'nationality')
        widgets = {
                'first_name': TextInput(attrs={'class': 'form-control'}),
                'last_name': TextInput(attrs={'class': 'form-control'}),
                'email': TextInput(attrs={'class': 'form-control'}),
                'phone_number': TextInput(attrs={'class': 'form-control'}),
                'address': TextInput(attrs={'class': 'form-control'}),
            }

        