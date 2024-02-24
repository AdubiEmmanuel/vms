from django.shortcuts import render, redirect
from django.utils import timezone

from django.contrib import auth
from django.contrib.auth.models import User
from .forms import UserForm, VendorCreateForm

from vms import settings 

# Create your views here.

def vendorLogin(request):
    return render(request,'Vendors/Auth/Login.html')

def vendorRegister(request):
    return render(request,'Vendors/Auth/Signup.html')