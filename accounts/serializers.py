from dataclasses import fields
from rest_framework import serializers
from .models import CustomUser



class UserLoginSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=128,min_length=6,write_only=True)

    class Meta:
        model=CustomUser
        fields=['email','password']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)    

class UserRegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=128,min_length=6,write_only=True)

    class Meta:
        model=CustomUser
        fields=['email','password']

          