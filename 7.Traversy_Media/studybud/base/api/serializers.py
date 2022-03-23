
#CLASSES that takes certain model to serialize object by turning it to JSON DATA

from rest_framework.serializers import ModelSerializer
from base.models import Room
class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
