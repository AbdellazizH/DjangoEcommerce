from django.conf.urls.static import static
from django.urls import path

from djangoProjectEcommerce import settings
from store import views

urlpatterns = [
    path('', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
