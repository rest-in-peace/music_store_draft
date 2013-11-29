# coding: utf-8

from rest_framework import serializers

from .models import Band, Song


class BandSerializer(serializers.HyperlinkedModelSerializer):
    albums_url = serializers.HyperlinkedIdentityField(
        view_name='band-album-list',
    )

    class Meta:
        model = Band
        fields = ('url', 'name', 'description', 'albums_url')


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
