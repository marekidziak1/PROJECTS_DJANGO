from .models import Course
from rest_framework.serializers import ModelSerializer

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'language', 'price')