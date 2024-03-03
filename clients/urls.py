from django.urls import path
from . import views 
from . views import clientRegister

urlpatterns = [
    path('cauth/login/', views.clientLogin, name='c_auth_login'),
    path('cauth/register/', clientRegister.as_view(), name='c_auth_register'),
    path('dashboard/', views.clientDashboard, name='dashboard'),
]
