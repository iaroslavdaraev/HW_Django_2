from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, VersionCreateView, VersionUpdateView, VersionDeleteView, VersionDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('version/create/', VersionCreateView.as_view(), name='create_version'),
    path('version/<int:pk>/', VersionDetailView.as_view(), name='version'),
    path('version/update/<int:pk>/', VersionUpdateView.as_view(), name='update_version'),
    path('version/delete/<int:pk>/', VersionDeleteView.as_view(), name='delete_version')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
