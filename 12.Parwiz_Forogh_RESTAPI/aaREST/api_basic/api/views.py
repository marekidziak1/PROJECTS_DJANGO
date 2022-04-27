from cgitb import lookup
from django.shortcuts import render

#from rest_framework.renderers import JSONRenderer 

from .serializers import ArticleSerializer, ArticleSerializerSerializer
from api_basic.models import Article

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from rest_framework import viewsets
class ArticleModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


from rest_framework import viewsets
from rest_framework import mixins
class ArticleGenericViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin, 
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()









from rest_framework import viewsets
from django.shortcuts import get_object_or_404
class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = ArticleSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    def update(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        try:
            article.delete()
        except:
            data ={'failure':'Object is not exist'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        else:
            data ={'success':'Object deleted'}
            return Response(data, status =status.HTTP_200_OK)












from rest_framework import generics
from rest_framework.generics import (ListAPIView, 
                                     CreateAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView)
class ListApiView(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
class CreateApiView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
class DetailApiView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field='id'
class UpdateApiView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field='id'
class DeleteApiView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field='id'


from rest_framework import generics
from rest_framework import mixins
class GenericAPIView(generics.GenericAPIView, 
                            mixins.ListModelMixin, 
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    #authentication_classes = [SessionAuthentication,BasicAuthentication]
    #permission_classes = [IsAuthenticated,]
    lookup_field = 'id'
    #jeżeli nie 'pk' tylko np 'id' to tworzysz zmienną: lookup_field = 'id'
    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)
    def post(self, request):
        return self.create(request)
    def put(self, request, id=None):
        return self.update(request, id)
    def delete(self, request, id=None):
        return self.destroy(request, id)


from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
class ArticleApiView(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(pk=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id=None):
        if id:
            article = self.get_object(id)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        else:
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data, status =status.HTTP_200_OK)
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_200_OK)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)
    def put(self,request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_200_OK)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        article = self.get_object(id)
        try:
            article.delete()
        except:
            data ={'failure':'Object is not exist'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        else:
            data ={'succesc':'Object deleted'}
            return Response(data, status =status.HTTP_200_OK)

class ArticleDetailApiView(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(pk=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    def put(self,request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_200_OK)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        article = self.get_object(id)
        try:
            article.delete()
        except:
            data ={'failure':'Object is not exist'}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        else:
            data ={'succesc':'Object deleted'}
            return Response(data, status =status.HTTP_200_OK)









@api_view(['GET','POST',])
def article_list_view(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
                                    #arg ' many=True ' oznacza że będzie serializacja 
									#więcej niż  jednego obiektu (cała lista/zbiór)
        return Response(serializer.data, status =status.HTTP_200_OK)
    elif request.method =='POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_200_OK)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE',])
def article_detail_view(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status =status.HTTP_404_NOT_FOUND )
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status =status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_200_OK)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status =status.HTTP_200_OK)

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['GET','POST',])
# def article_list_view(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#                                     #arg ' many=True ' oznacza że będzie serializacja 
# 									#więcej niż  jednego obiektu (cała lista/zbiór)
#         return Response(serializer.data, status =status.HTTP_200_OK)
#     elif request.method =='POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status =status.HTTP_200_OK)
#         return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE',])
# def article_detail_view(request,pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(status =status.HTTP_404_NOT_FOUND )
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data, status =status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status =status.HTTP_200_OK)
#         return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status =status.HTTP_200_OK)







# @csrf_exempt
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method =='POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status = 201)
#         return JsonResponse(serializer.errors, status = 400)

# @csrf_exempt
# def article_detail(request,pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status = 404)
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(data = serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status = 201)
#         return JsonResponse(serializer.errors, status = 400)
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status = 200)