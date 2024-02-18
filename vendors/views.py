from django.shortcuts import render, redirect
from django.utils import timezone

from django.contrib import auth
from django.contrib.auth.models import User
from .forms import UserForm, VendorCreateForm

from vms import settings 

# Create your views here.

def intern_profile_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='UF')
        vendor_form = VendorCreateForm(request.POST, prefix='PF')
	
    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save(commit=False)
        user.save()
        
        user.vendor_form.bio = profile_form.cleaned_data.get('bio')
        user.intern_profile.location = profile_form.cleaned_data.get('location')
        user.intern_profile.save()
    else:
        user_form = UserForm(prefix='UF')
        profile_form = InternProfileForm(prefix='PF')
        
    return render(request, 'intern/intern_profile.html',{
			'user_form': user_form,
			'profile_form': profile_form,
		})