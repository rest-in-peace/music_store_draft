
from django.shortcuts import render

from rest_framework import generics

from albums.models import Album
from albums.serializers import AlbumSerializer, AlbumTracksSerializer


class AlbumListAPIView(generics.ListAPIView):
    model = Album
    serializer_class = AlbumSerializer


class AlbumRetrieveAPIView(generics.RetrieveAPIView):
    model = Album
    serializer_class = AlbumSerializer


class AlbumTracksAPIView(generics.RetrieveAPIView):
    model = Album
    serializer_class = AlbumTracksSerializer

