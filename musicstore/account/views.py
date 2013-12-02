# coding: utf-8

from django.contrib.auth.models import User

from rest_framework import generics

from . import serializers


class UserCreateAPIView(generics.CreateAPIView):
    '''
    API endpoint to register new users
    '''
    model = User
    serializer_class = serializers.CreateUserSerializer
