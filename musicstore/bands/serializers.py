# coding: utf-8

from rest_framework import serializers

from .models import Band


class BandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Band
