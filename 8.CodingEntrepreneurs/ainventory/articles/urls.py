
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.article_search_view, name="search"),
    path('<int:id>/', views.article_detail_view),
    path("searched/",views.searched_view),
    path('create/',views.article_create_view, name="create"),
]
