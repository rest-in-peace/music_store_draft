
from django.shortcuts import render

from rest_framework import generics
from model_mommy import mommy

from .models import Purchase
from .serializers import TrackPurchaseSerializer


class TrackPurchaseView(generics.CreateAPIView):
    model = Purchase
    serializer_class = TrackPurchaseSerializer

    def get_serializer(self, data=None, *args, **kwargs):
        data = data.copy()

        # replace with current user
        data['user'] = mommy.make('auth.User').id
        data['track'] = self.kwargs['pk']

        return super(TrackPurchaseView, self).get_serializer(data=data, *args, **kwargs)
