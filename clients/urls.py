from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 
from . views import clientRegister

urlpatterns = [
    path('cauth/login/', views.clientLogin, name='c_auth_login'),
    path('cauth/register/', clientRegister.as_view(), name='c_auth_register'),
    path('cdashboard/', views.clientDashboard, name='c_dashboard'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
