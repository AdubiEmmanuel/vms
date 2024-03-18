from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Product
from .forms import ProductForm
from django.views import View

# Create your views here.

def product(request):
    form = ProductForm()
    template = 'Vendors/Dashboard/index.html'
    return render(request, template, {'form':form})


