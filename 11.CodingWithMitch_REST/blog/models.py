from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
# Create your models here.

        
class BlogPost(models.Model):
    title           = models.CharField(max_length=50, null=False, blank=False)
    body            = models.TextField(max_length=5000, null=False, blank=False)
    image           = models.ImageField(upload_to='blog_images', null=False, blank=False)
    date_published  = models.DateTimeField(auto_now_add=True, verbose_name="date_published")
    date_updated    = models.DateTimeField(auto_now = True, verbose_name="date_updated")
    author          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug            = models.SlugField(null=True,unique=True, blank=True)
    def __str__(self):
        return self.title


@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance, *args, **kwargs):
    instance.image.delete(False)

def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-"+instance.title)

pre_save.connect(pre_save_blog_post_receiver, sender = BlogPost)