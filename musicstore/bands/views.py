# coding: utf-8

from rest_framework import generics

from .models import Band


class BandListAPIView(generics.ListAPIView):
    '''
    This API endpoint presents a list of bands.
    '''
    model = Band
