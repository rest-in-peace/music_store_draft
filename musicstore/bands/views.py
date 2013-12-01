# coding: utf-8

from rest_framework import generics

from albums.models import Album
from songs.models import Song

from .models import Band
from . import serializers


class BandListAPIView(generics.ListCreateAPIView):
    '''
    This API endpoint presents a list of bands.
    '''
    model = Band
    serializer_class = serializers.BandSerializer


class BandDetailAPIView(generics.RetrieveAPIView):
    '''
    This API endpoint presents a bands.
    '''
    model = Band
    serializer_class = serializers.BandSerializer


class BandAlbumListAPIView(generics.ListAPIView):
    '''
    This API endpoint presents a list of albums of a band
    '''
    model = Album

    def get_queryset(self):
        qs = super(BandAlbumListAPIView, self).get_queryset()
        return qs.filter(band=self.kwargs['pk'])
