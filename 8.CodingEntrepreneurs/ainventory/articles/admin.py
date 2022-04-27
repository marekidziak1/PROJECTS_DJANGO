from dataclasses import fields
from django.contrib import admin
from .models import Article 
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','slug','timestamp','updated']
    search_fields =['title','content']
    fields =['title','slug','content','publish']
    #prepopulated_fields = {'slug':('title',)}
admin.site.register(Article, ArticleAdmin)
