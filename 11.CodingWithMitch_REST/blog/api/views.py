from rest_framework import status
from rest_framework.response import Response
from .serializers import BlogPostSerializer#, BlogPostUpdateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from blog.models import BlogPost
from account.models import Account
from django.contrib.auth.decorators import login_required

from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView

#@login_required(login_url='login')
@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def api_detail_blog_view(request, slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method =="GET":
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT',])
@permission_classes((IsAuthenticated, ))
def api_update_blog_view(request, slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    user = request.user
    if blog_post.author != user:
        return Response({'response':"You don't have permission to edit that"}) 
    if request.method =="PUT":
        serializer = BlogPostSerializer(blog_post, data=request.data, partial=True)
        data={}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
@permission_classes((IsAuthenticated, ))
def api_delete_blog_view(request, slug):
    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    user = request.user
    if blog_post.author != user:
        return Response({'response':"You don't have permission to delete that"}) 
    if request.method =="DELETE":
        operation=blog_post.delete()
        data={}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)

@api_view(['POST',])
@permission_classes((IsAuthenticated, ))
def api_create_blog_view(request):
    account = request.user
    blog_post = BlogPost(author=account)   #(author=account.user)
    if request.method == 'POST':
        serializer = BlogPostSerializer(blog_post, data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiBlogListView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    #authentication_classes = (SessionAuthentication, BasicAuthentication)#(TokenAuthentication,)
    permission_classes = (IsAuthenticated,)     #(AllowAny,)        #
    pagination_class = PageNumberPagination
    page_size = 1
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title','body', 'author__username','author__email')