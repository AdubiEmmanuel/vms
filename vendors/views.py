from django.shortcuts import render, redirect
from django.utils import timezone

from django.contrib import auth
from django.contrib.auth.models import User
from .forms import VendorForm
from django.views import View

from vms import settings 

# Create your views here.

def vendorLogin(request):
    return render(request,'Vendors/Auth/Login.html')

def vendorDashboard(request):
    template = 'Vendors/Dashboard/index.html'
    return render(request, template)


class VendorRegister(View):
    template_name = 'Vendors/Auth/Signup.html'

    def get(self, request):
        form = VendorForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        vendor_dashboard = 'dashboard'
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add additional logic here, e.g., redirecting to a success page
            return redirect(vendor_dashboard)
        return render(request, self.template_name, {'form': form})