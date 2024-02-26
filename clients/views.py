from django.shortcuts import render, redirect
from django.utils import timezone

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Client 
from .forms import ClientForm
from django.shortcuts import render, redirect
from django.views import View



from vms import settings 


# Create your views here.

def clientLogin(request):
    return render(request, 'Clients/Auth/Login.html')

def clientDashboard(request):
    template = 'Clients/Dashboard/index.html'
    return render(request, template)


class clientRegister(View):
    template_name = 'Clients/Auth/Signup.html'

    def get(self, request):
        form = ClientForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        client_dashboard = 'client/dashboard/index.html'
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add additional logic here, e.g., redirecting to a success page
            return redirect(client_dashboard)
        return render(request, self.template_name, {'form': form})