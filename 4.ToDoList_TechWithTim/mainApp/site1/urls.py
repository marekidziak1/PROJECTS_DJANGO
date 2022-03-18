from django.urls import path
from . import views 

urlpatterns=[
    #path("<int:id>", views.index, name='index'),
    path("", views.home, name='home'),
    path("home/", views.home, name='home'),
    path("<int:id>/", views.index, name='index'),
    #path("<int:id>/", views.list, name='list'),
    path("create/", views.create, name='create'),
    path("view/", views.view, name='view'),










    path("<int:my_pk>/v", views.v1, name='v1'),
    path("item/<int:my_pk>/v", views.v2, name='v2'),
    path("items/<str:my_name>/v", views.v3, name='v3'),
]