from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index_homepage, contacts

urlpatterns = [
    path('', index_homepage),
    path('contacts/', contacts)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
