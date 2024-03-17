from django.urls import path

from catalog.views import index_homepage, contacts

urlpatterns = [
    path('', index_homepage),
    path('contacts/', contacts)
]
