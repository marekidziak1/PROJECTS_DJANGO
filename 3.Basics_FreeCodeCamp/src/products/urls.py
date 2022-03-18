
from django.urls import path
from . import views as products_views

app_name = 'products'
urlpatterns=[
    path('', products_views.product_list_view, name='product_list'),
    path('<int:my_id>/', products_views.product_detail_view, name='product_detail'),
    path('<int:my_id>/delete/', products_views.product_delete_view, name='product_delete'),
    path('<int:my_id>/update/', products_views.product_update_view, name='product_update'),
    path('create/',products_views.product_create_view, name='product_create'),

    path('create_basic/', products_views.product_create_raw_view, name='product_create_basic'),
    path('create_basic_form/', products_views.product_basic_form_view, name='basic_form'),
]