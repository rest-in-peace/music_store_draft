# coding: utf-8

from django.test import TestCase

from rest_framework.test import APIRequestFactory
from model_mommy import mommy

from bands import views


factory = APIRequestFactory()


class TestBandView(TestCase):
    def setUp(self):
        self.view = views.BandListAPIView.as_view()

    def test_list_band_view_should_return_200(self):
        request = factory.get('/')
        response = self.view(request).render()
        self.assertEqual(response.status_code, 200)

    def test_it_should_return_a_list_of_bands(self):
        mommy.make('bands.Band', name='Beatles')

        request = factory.get('/')
        response = self.view(request).render()
        self.assertEqual(response.data[0]['name'], 'Beatles')

