from django.urls import path, include
#from .views import article_list, article_detail
from .views import (
    article_list_view, 
    article_detail_view,
    ArticleApiView,
    GenericAPIView,
    ListApiView,
    CreateApiView,
    DetailApiView,
    UpdateApiView,
    DeleteApiView,
    ArticleViewSet,
    ArticleGenericViewSet,
    ArticleModelViewSet,
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('article', ArticleViewSet, basename = 'article')
router.register('genericArticle', ArticleGenericViewSet, basename='genericArticle')
router.register('modelArticle', ArticleModelViewSet, basename='modelArticle')

urlpatterns =[
    path('article/', article_list_view),
    path('article/<int:pk>/', article_detail_view),
    path('classBasedViewArticle/', ArticleApiView.as_view()),
    path('classBasedViewArticle/<int:id>/', ArticleApiView.as_view()),
    path('genericsMixins/', GenericAPIView.as_view()),
    path('genericsMixins/<int:id>/', GenericAPIView.as_view()),
    path('auth/',include('rest_framework.urls')),
    path('list/', ListApiView.as_view()),
    path('create/', CreateApiView.as_view()),
    path('detail/<int:id>/', DetailApiView.as_view()),
    path('update/<int:id>/', UpdateApiView.as_view()),
    path('delete/<int:id>/', DeleteApiView.as_view()),
    #----------------------------------------------------
    path('viewset/', include(router.urls)),
]