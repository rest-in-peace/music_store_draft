
from rest_framework import serializers

from .models import Track


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    was_bought = serializers.IntegerField('was_bought', read_only=True)
    download_count = serializers.IntegerField('download_count', read_only=True)

    class Meta:
        model = Track
        fields = (
            'url', 'song', 'album', 'price', 'track_file', 'was_bought',
            'download_count',
        )


class TrackListSerializer(serializers.ModelSerializer):
    song_name = serializers.CharField(source='song.name', read_only=True)

    class Meta:
        model = Track
        fields = ('song_name', 'price',)
