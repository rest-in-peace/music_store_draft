# coding: utf-8

from django.core.urlresolvers import reverse

from rest_framework.test import APIRequestFactory, APIClient, APITestCase
from model_mommy import mommy

from purchases import views


factory = APIRequestFactory()
client = APIClient()


class TestTrackPurchase(APITestCase):

    def setUp(self):
        super(TestTrackPurchase, self).setUp()

        self.track = mommy.make('tracks.Track')
        self.view = views.TrackPurchaseView.as_view()
        self.url = reverse('purchase-track', kwargs={'pk': self.track.pk})

    def test_track_purchase_view_should_return_201(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 201)
