# coding: utf-8

from rest_framework import serializers

from .models import Purchase


class TrackPurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = ('user', 'track')
