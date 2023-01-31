

from user_accounts.models import *
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework import status


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    password = serializers.CharField(style={'input_type': 'password'},write_only=True)
    uuid = serializers.UUIDField(read_only = True)
    
    class Meta:
        model = CustomUser
        fields = ['uuid','password','password2','username','first_name','last_name','is_staff','date_of_birth','email','phone','address','secondary_email','is_active']
        
    
class UserLoginSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField()
    password = serializers.CharField()

    
    class Meta:
        model = CustomUser
        fields = ['username','password'] #username is email
        
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect username and password")

        
class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    def create(self, validated_data):
        p=validated_data['user'].get('password')
        p2=validated_data['user'].get('password2')
        if p == p2:
            validated_data["user"].pop("password2")
            user = CustomUser.objects.create(**validated_data["user"])
            user.save()
            staff_member = Staff.objects.create(user=user)
        else:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return staff_member

    


    class Meta:
        model = Staff
        fields = '__all__'
        
        
        

        

        
        
        
        

        

        
        
