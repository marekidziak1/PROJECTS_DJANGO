from django.urls import path, include
#from .views import article_list, article_detail
from .views import article_list_view, article_detail_view
urlpatterns =[
    path('article', article_list_view),
    path('article/<int:pk>', article_detail_view),
    path('api/', include('api_basic.api.urls')),
]