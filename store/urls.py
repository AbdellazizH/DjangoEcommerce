from django.conf.urls.static import static
from django.urls import path

from djangoProjectEcommerce import settings
from store import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<str:slug>/', views.product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
