
from django.contrib import admin
from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    path("", views.article_search_view, name="search"),
    path("searched/",views.searched_view),
    path('<slug:slug>/', views.article_detail_view, name='detail'),
    path('create/',views.article_create_view, name="create"),
]
