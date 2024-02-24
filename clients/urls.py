from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.clientLogin, name='clientLogin'),
    path('register/', views.clientRegister, name='clientRegister'),
]
