from django.urls import path, include
from . import views as registerViews
urlpatterns = [
    path("", registerViews.register, name='register'),
]