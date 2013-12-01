# coding: utf-8

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    '''
    The entry endpoint of our API.
    '''
    return Response({
        'albums': reverse('album-list', request=request),
        'bands': reverse('band-list', request=request),
        'songs': reverse('song-list', request=request),
    })
