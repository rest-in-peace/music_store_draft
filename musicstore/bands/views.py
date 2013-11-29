# coding: utf-8

from rest_framework import generics

from .models import Band
from .serializers import BandSerializer


class BandListAPIView(generics.ListAPIView):
    '''
    This API endpoint presents a list of bands.
    '''
    model = Band
    serializer_class = BandSerializer


class BandDetailAPIView(generics.RetrieveAPIView):
    model = Band
    serializer_class = BandSerializer
