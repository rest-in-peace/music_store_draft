# coding: utf-8

from django.shortcuts import render

from rest_framework import generics

from .models import Song
from . import serializers


class SongListAPIView(generics.ListCreateAPIView):
    '''
    This API endpoint presents a list of songs.
    '''
    model = Song
    serializer_class = serializers.SongSerializer


class SongDetailAPIView(generics.RetrieveUpdateAPIView):
    '''
    This API endpoint presents a list of songs.
    '''
    model = Song
    serializer_class = serializers.SongSerializer
