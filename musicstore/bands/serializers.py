# coding: utf-8

from rest_framework import serializers

from albums.serializers import BandAlbumSerializer
from .models import Band


class BandSerializer(serializers.HyperlinkedModelSerializer):
    albums_url = serializers.HyperlinkedIdentityField(
        view_name='band-album-list',
    )
    albums = BandAlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Band
        fields = ('url', 'name', 'description', 'albums', 'albums_url')
