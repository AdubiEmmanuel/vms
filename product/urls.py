from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views 


urlpatterns = [
    path('create/', views.product_create, name='create_product'),
    path('<int:pk>/update/', views.product_update, name='update_product'),
    path('list/product', views.product_list, name='list_product'),
    path('<int:pk>/update/', views.product_delete, name='delete_product'),
    path('<int:pk>/', views.product_detail, name='detail_product'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)