from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import *


class IdSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Id'
        fields = '__all__'
      
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Id','username','Email']
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password','email']
            
        def create(self,validated_data):
            user = User.objects.create_user(**validated_data)
            return user 
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
        
    def user(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Invalid Credentials')
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Subject'
        fields = '__all__'
        
class HoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Hours_Studied'
        fields = '__all__'
        
class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Date'
        fields = '__all__'
        
class Created_atSerializer(serializers.ModelSerializer):
    model = 'Created_at'
    fields = '__all__'