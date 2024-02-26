from django.urls import path
from . import views 
from . views import clientRegister

urlpatterns = [
    path('login/', views.clientLogin, name='login'),
    path('register/', clientRegister.as_view(), name='register'),
    path('dashboard/', views.clientDashboard, name='dashboard'),
]
