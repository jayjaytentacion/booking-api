
from django.shortcuts import render
from rest_framework import generics
from accounts.models import CustomUser

from accounts.serializers import UserLoginSerializer,UserRegisterSerializer

# Create your views here.

class UserLoginView(generics.GenericAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserLoginSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserRegisterSerializer

