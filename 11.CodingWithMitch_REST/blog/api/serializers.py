from django.forms import ValidationError
from rest_framework import serializers
from blog.models import BlogPost
class BlogPostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_author')
    #image = serializers.SerializerMethodField('validate_image_url')
    class Meta:
        model = BlogPost
        fields = ['title','body', 'image','username']
    def get_username_from_author(self, blog_post):
        username = blog_post.author.username
        return username
    # def validate_image_url(self, blog_post):
    #     image = blog_post.image
    #     new_url = image.url
    #     if '?' in new_url:
    #         new_url = image.url[:image.url.rfind('?')]
    #     return new_url

# import cv2                         #musisz zainstalować opencv: pip3 install opencv-python
# import sys
# import os
# from django.conf import settings
# from django.core.files.storage import default_storage
# from django.core.files.storage import FileSystemStorage
# IMAGE_SIZE_MAX_BYTES = 1024 *1024 *2 #2mb
# MIN_TITLE_LENGTH = 5
# MIN_BODY_LENGTH = 50
# class BlogPostUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BlogPost
#         fields = ['title','body','image']
#     def validate(self, blog_post):
#         try:
#             title = blog_post['title']
#             if len(title) < MIN_TITLE_LENGTH:
#                 raise serializers.ValidationError({'response':"Enter a title longer than: " + str(MIN_TITLE_LENGTH)})
#             body = blog_post['body']
#             if len(body) < MIN_BODY_LENGTH:
#                 raise serializers.ValidationError({'response':"Enter a body longer than: " + str(MIN_BODY_LENGTH)})
            
#             image = blog_post["image"]     
#             url = os.path.join(settings.TEMP, str(image))   #musisz stworzyć folder 'temp' w aplikacjach
#             storage = FileSystemStorage(location=url)
#             with storage.open('','wb+') as destination:
#                 for chunk in image.chunks():
#                     destination.write(chunk)
#                 destination.close()
            
#             if sys.getsizeof(image.file) > IMAGE_SIZE_MAX_BYTES:
#                 os.remove(url)
#                 raise serializers.ValidationError({'response':"that image is to big"})
            
#             img = cv2.imread(url)
#             dimensions = img.shape

#             aspect_ratio = dimensions[1] / dimensions[2]    #divide with / height
#             if aspect_ratio <1:
#                 os.remove(url)  
#                 raise serializers.ValidationError({'response':"Image height "})
#             os.remove(url)
#         except KeyError:
#             pass 
#         return blog_post

# class BlogPostCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BlogPost
#         fields = ['title','body','image','date_updated','author']
#     def save(self):
#         try:
#             title = self.validated_data['title']
#             if len(title) < MIN_TITLE_LENGTH:
#                 raise serializers.ValidationError({'response':"Enter a title longer than: " + str(MIN_TITLE_LENGTH)})
#             body = self.validated_data['body']
#             if len(body) < MIN_BODY_LENGTH:
#                 raise serializers.ValidationError({'response':"Enter a body longer than: " + str(MIN_BODY_LENGTH)})
#             image= self.validated_data['image']
#             author = self.validated_data['author']
#             blog_post=BlogPost(title, body, image, author)
#         except KeyError:
#             pass 
#         return blog_post