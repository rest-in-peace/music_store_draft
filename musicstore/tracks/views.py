# coding: utf-8

from rest_framework import generics

from .models import Track
from . import serializers


class TrackListAPIView(generics.ListCreateAPIView):
    '''
    This API endpoint presents a list of tracks.
    '''
    queryset = Track.objects.order_by('-id')
    serializer_class = serializers.TrackSerializer


class TrackDetailAPIView(generics.RetrieveUpdateAPIView):
    '''
    This API endpoint presents a tracks.
    '''
    model = Track
    serializer_class = serializers.TrackSerializer
