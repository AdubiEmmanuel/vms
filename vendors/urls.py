from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.vendorLogin, name='vendorLogin'),
    path('register/', views.vendorRegister, name='vendorRegister'),
]
