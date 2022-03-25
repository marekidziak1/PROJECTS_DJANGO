from django.db import models

class Article (models.Model):
    title = models.TextField(unique=True)
    content = models.TextField()
    def __str__(self):
        return self.title