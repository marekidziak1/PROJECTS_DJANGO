from venv import create
from django.urls import path
from .views import home, contact, products, customer, createOrder, updateOrder, deleteOrder


urlpatterns = [
    path('', home, name='home'),
    path('customer/<str:pk>/', customer, name='customer'),
    path('products/', products, name='products'),
    path('create_order/<str:pk>', createOrder, name="create_order"),
    path('update_order/<str:pk>/', updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', deleteOrder, name="delete_order"),
]