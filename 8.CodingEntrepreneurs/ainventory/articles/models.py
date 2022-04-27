from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify 
from .utils import my_slugify

class ArticleQuerySet(models.QuerySet):
     def search2(self, query):
        if query is not None:
            return self.filter(Q(title__icontains=query) | Q(content__icontains=query))
        else:
            return self.none()   #zwróci pustą listę
class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, self._db)
    def search(self, query):
        return self.get_queryset().search2(query)   #zwróci pustą listę

# class ArticleManager(models.Manager):
#     def search(self, query):
#         if query is not None:
#             #return Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
#             return self.get_queryset().filter(Q(title__icontains=query) | Q(content__icontains=query))
#         else:
#             return self.get_queryset().none()   #zwróci pustą listę

class Article(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length =120 ,unique=True)
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now= True)
    publish = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    objects = ArticleManager()
    # def save(self):
    #     self.slug = slugify(self.title)
    #     super().save()
# import random
# def my_slugify(instance):
#     my_slug = f'{slugify(instance.title)}-{random.randint(300000,500000)}'
#     qs =Article.objects.filter(slug__exact=my_slug).exclude(id=instance.id)
#     if qs.exists():
#         return my_slugify(instance)
#     return my_slug
    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'slug':self.slug})
def article_post_save(sender, instance, created, *args,**kwargs):
    my_slug = my_slugify(instance)
    if instance.slug is None:
        instance.slug=my_slug
        instance.save()
    
post_save.connect(article_post_save, sender=Article)