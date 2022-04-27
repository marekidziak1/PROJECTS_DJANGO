from django.shortcuts import render, redirect
from account.models import Account
from rest_framework.authtoken.models import Token


from rest_framework import status
from rest_framework.response import Response 

from .serializers import RegistrationSerializer, AccountPropertiesSerializer, ChangePasswordSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from django.contrib.auth import authenticate

class ObtainAuthTokenView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        data = {}
        email = request.POST.get('email')  #dla funkcji obtain_auth_token z rest_framework.authtoken.views musisałeś podać w 
                                              #żadaniu POST parametr o kluczu 'username' ale teraz możesz podać normalny parametr
        password = request.POST.get('password')  
        account = authenticate(email=email, password = password) 
        if account:
            token=Token.objects.get_or_create(user=account)         #if user is loged in and somehow doesn't have a token
            data['response'] = 'Succesfully authenticated'
            data['pk'] = account.pk
            data['email'] = email
            data['token'] = token[0].key
        else:
            data['response'] = 'Error'
            data['error_message'] = 'Invalid credentials'
        return Response(data=data)



@api_view(['POST',])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "succesfully registersa new user"
        data['email'] = account.email
        data['username'] = account.username
        s = status.HTTP_201_CREATED
        data['token'] = Token.objects.get(user=account).key
    else:
        data = serializer.errors
        s = status.HTTP_400_BAD_REQUEST
    return Response(data=data, status = s)

@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def account_properties_view(request):
    try:
        account=request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AccountPropertiesSerializer(account)
        return Response(serializer.data)

@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def account_update_view(request):
    try:
        account=request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = RegistrationSerializer(instance=account, data = request.data)
        data ={} 
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Account update success"
            return Response(data=data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def account_delete_view(request):
    try:
        account=request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        operation=account.delete()
        data={}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)

@api_view(['GET',])
@permission_classes([])
def does_account_exist_view(request):
    email = request.GET['email']
    data={}
    try:
        email=email.lower()
        account = Account.objects.get(email=email)
        data['response'] = email
    except Account.DoesNotExist:
        data['response'] = "Account does not exist"
    return Response(data=data)


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = Account
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            #check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password":["Wrong password. "]}, status = status.HTTP_400_BAD_REQUEST)
            #confirm the new passwords match
            new_password = serializer.data.get("new_password")
            confirm_new_password = serializer.data.get("confirm_new_password")
            if new_password != confirm_new_password:
                return Response({"new_password": ["New passwords must be the same "]}, status = status.HTTP_400_BAD_REQUEST)
            #set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"reponse":"succesfully changed password"}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)