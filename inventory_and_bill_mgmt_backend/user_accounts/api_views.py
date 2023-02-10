from django.shortcuts import HttpResponse, render, HttpResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User

from user_accounts.models import CustomUser, Staff

from .serializers import *


from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import permission_required
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import authenticate
import json
from rest_framework.permissions import DjangoModelPermissions


def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

# # Create your views here.
class UserList(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [JWTAuthentication]
   # permission_classes = [DjangoModelPermissions]
    
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)


class LoginViewSet(viewsets.ModelViewSet):
    
    queryset = CustomUser.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes=[AllowAny]

    
   
    def list(self, request, *args, **kwargs):
        return Response({"error":"login_required"})
    

    def create(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        
        # username = serializer.data.get('username')
        # password = serializer.data.get('password')
        # user = authenticate(username=username, password=password)
        # if user is not None:
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':f'Login Success', 'uuid': user.uuid}, status=status.HTTP_200_OK)
        # else:
            # return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
    
    
    
from django.db import IntegrityError
class StaffCreatViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes=[DjangoModelPermissions]
     
    # def create(self, request, *args, **kwargs):
    #     serializer=self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = User.objects.create(email=serializer.validated_data['email'], name=serializer.validated_data['name'],
    #                                 password=serializer.validated_data['password'])
    #     staff_member = Staff.objects.create(user=user)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance= self.get_object()
        serializer=self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        serializer = self.get_serializer(instance, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # def patch(self, request, pk):
    #     instance = self.get_object(pk)
    #     data= request.data
    #     serializer = self.get_serializer(instance, data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.delete(instance)
        except:
            pass
        return Response(status=status.HTTP_404_NOT_FOUND)

    

