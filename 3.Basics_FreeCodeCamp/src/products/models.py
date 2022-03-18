from django.urls import reverse
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price=models.DecimalField(decimal_places=2, max_digits=10000)
    summary=models.TextField()
    featured = models.BooleanField()

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id":self.id})