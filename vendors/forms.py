from django import forms
from django.contrib.auth.models import User 
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.forms import  UserCreationForm
from .models import Vendor 

class VendorForm(UserCreationForm):
    location_countries = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location_cities = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
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


        