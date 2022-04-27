from django.urls import include, path
from . import views as courses_views
urlpatterns =[
    path('',courses_views.getCourses, name='getCourses')
]