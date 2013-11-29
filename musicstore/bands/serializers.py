# coding: utf-8

from rest_framework import serializers

from .models import Band, Song


class BandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Band


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
