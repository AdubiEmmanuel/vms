from django.shortcuts import render, redirect
from django.utils import timezone

from django.contrib import auth
from django.contrib.auth.models import User


from vms import settings 

# Create your views here.

def clientLogin(request):
    return render(request, 'Clients/Auth/Login.html')


def clientRegister(request):
    return render(request, 'Clients/Auth/Signup.html')