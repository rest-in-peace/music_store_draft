# coding: utf-8

from rest_framework import generics

from .models import Band, Song, Album
from . import serializers


class BandListAPIView(generics.ListAPIView):
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


class SongListAPIView(generics.ListAPIView):
    '''
    This API endpoint presents a list of songs.
    '''
    model = Song
    serializer_class = serializers.SongSerializer


class SongDetailAPIView(generics.RetrieveAPIView):
    '''
    This API endpoint presents a list of songs.
    '''
    model = Song
    serializer_class = serializers.SongSerializer
