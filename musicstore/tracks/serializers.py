
from rest_framework import serializers

from .models import Track


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Track


class TrackListSerializer(serializers.ModelSerializer):
    song_name = serializers.CharField(source='song.name', read_only=True)

    class Meta:
        model = Track
        fields = ('song_name', 'price')
