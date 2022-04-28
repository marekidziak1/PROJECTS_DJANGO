from django.urls import path
from .views import home, contact, products, customer


urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('customer/', customer),
    path('products/', products),
]