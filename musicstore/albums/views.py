
from django.shortcuts import render

from rest_framework import generics

from albums.models import Album
from albums.serializers import AlbumSerializer, AlbumTracksSerializer

from comments.views import BaseCommentListAPIView


class AlbumListAPIView(generics.ListCreateAPIView):
    model = Album
    serializer_class = AlbumSerializer


class AlbumRetrieveAPIView(generics.RetrieveUpdateAPIView):
    model = Album
    serializer_class = AlbumSerializer


class AlbumTracksAPIView(generics.RetrieveAPIView):
    model = Album
    serializer_class = AlbumTracksSerializer


class AlbumCommentListAPIView(BaseCommentListAPIView):
    ctype_model = Album
