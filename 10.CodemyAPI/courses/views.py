from operator import truediv
from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializer
from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def getCourses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    #serializer = serialize('json', courses)
    return Response(serializer.data)
