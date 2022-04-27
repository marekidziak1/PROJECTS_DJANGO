#from .models import Article
from django.utils.text import slugify 
import random
def my_slugify(instance):
    my_slug = f'{slugify(instance.title)}-{random.randint(300000,500000)}'
    Klass = instance.__class__
    qs =Klass.objects.filter(slug__exact=my_slug).exclude(id=instance.id)
    if qs.exists():
        return my_slugify(instance)
    return my_slug