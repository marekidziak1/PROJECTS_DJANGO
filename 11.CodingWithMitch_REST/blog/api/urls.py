from django.urls import path, include

from blog.api.views import (api_detail_blog_view, 
                            api_update_blog_view,
                            api_delete_blog_view,
                            api_create_blog_view,
                            ApiBlogListView,
                            )

app_name='blog'

urlpatterns = [
    path("<slug:slug>/", api_detail_blog_view, name="detail"),
    path("<slug:slug>/update/", api_update_blog_view, name="update"), 
    path("<slug:slug>/delete/", api_delete_blog_view, name="delete"),
    path("create", api_create_blog_view, name="create"),    #przy POST w create w linku i w postmanie musi byc BEZ slasha na końcu!!!
    path("list", ApiBlogListView.as_view(), name = "list"),
]

