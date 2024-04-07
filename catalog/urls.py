from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index_homepage, contacts, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index_homepage, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:id>/', product, name='product')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
