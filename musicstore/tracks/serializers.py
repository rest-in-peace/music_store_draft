
from rest_framework import serializers

from .models import Track


class TrackListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = ('price',)
