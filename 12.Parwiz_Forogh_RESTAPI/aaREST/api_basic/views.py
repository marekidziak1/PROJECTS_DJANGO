from django.shortcuts import render

#from rest_framework.renderers import JSONRenderer 

from .serializers import ArticleSerializer
from .models import Article

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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