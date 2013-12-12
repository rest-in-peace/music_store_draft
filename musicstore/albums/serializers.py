
from rest_framework import serializers

from albums.models import Album
from tracks.serializers import TrackListSerializer


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album


class AlbumTracksSerializer(serializers.ModelSerializer):
    tracks = TrackListSerializer(many=True)

    class Meta:
        model = Album
        fields = ('title', 'tracks',)


class BandAlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ('url', 'title')
