from django.urls import path
from . import views 
from . views import VendorRegister

urlpatterns = [
    path('v_auth/login/', views.vendorLogin, name='v_auth_login'),
    path('v_auth/register/', VendorRegister.as_view(), name='v_auth_register'),
]
