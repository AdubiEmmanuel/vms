from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 


urlpatterns = [
    path('create/product', views.product, name='create_product'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)