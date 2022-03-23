from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from . serializers import RoomSerializer

#getRoutes nie jest potrzebne - po prostu wskazuję jakie masz ścieżki 
@api_view(['GET'])      #users can only GET data without sending them
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return Response(routes)
    #return Response(routes) - RESPONSE can NOT return PYTHON OBJECTS --> you need to serialize data.

from django.core.serializers import serialize
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many = True) #many =True means that we gonna serilize NOT a single object 
    #serializer = serialize('json',rooms)
    return Response(serializer)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many = False) #many =True means that we gonna serilize NOT a single object 
    return Response(serializer.data)

'''
from django.http import JsonResponse
import json
from django.core.serializers import serialize
def getMyRooms(request):
    rooms = Room.objects.all()
    rooms_serialize = json.loads(serialize('json',rooms))
    return JsonResponse(rooms_serialize, safe=False)   
from django.http import JsonResponse
#1
def getRoutes(request):
    #View that shows all routes in api
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',

    ]
    return JsonResponse(routes, safe=False)     
        #safe=False - allows giving an argumnent as not Dictionary 
        #(e.g: list), and JsonResponse convert this list as Dictionary
     '''