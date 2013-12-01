# coding: utf-8

from django.test import TestCase

from rest_framework.test import APIRequestFactory
from model_mommy import mommy

from bands import views


factory = APIRequestFactory()


class TestBandListView(TestCase):
    def setUp(self):
        mommy.make('bands.Band', name='Beatles')
        self.view = views.BandListAPIView.as_view()

        self.data = {
            'name': 'kraftwerk', 'description': 'German electronic music band',
        }

    def test_list_band_view_should_return_200(self):
        request = factory.get('/')
        response = self.view(request).render()
        self.assertEqual(response.status_code, 200)

    def test_it_should_return_a_list_of_bands(self):
        request = factory.get('/')
        response = self.view(request).render()
        self.assertEqual(response.data[0]['name'], 'Beatles')

    def test_endpoint_should_contain_url_to_detail(self):
        request = factory.get('/')
        response = self.view(request).render()
        self.assertEqual(response.data[0]['url'], 'http://testserver/bands/1/')

    def test_endpoint_should_contain_ur_to_albums_from_band(self):
        request = factory.get('/')
        response = self.view(request, pk=1).render()
        self.assertEqual(
            response.data[0]['albums_url'],
            'http://testserver/bands/1/albums/',
        )

    def test_create_new_band(self):
        request = factory.post('/', data=self.data, format='json')
        response = self.view(request).render()
        self.assertEqual(response.status_code, 201)

class TestBandDetailView(TestCase):
    def setUp(self):
        mommy.make('bands.Band', name='Beatles')
        self.view = views.BandDetailAPIView.as_view()

    def test_band_detail_should_return_200(self):
        request = factory.get('/')
        response = self.view(request, pk=1).render()
        self.assertEqual(response.status_code, 200)

    def test_band_detail_shourl_contain_url_to_detail_itself(self):
        request = factory.get('/')
        response = self.view(request, pk=1).render()
        self.assertEqual(response.data['url'], 'http://testserver/bands/1/')


class TestBandAlbumListView(TestCase):
    def setUp(self):
        self.view = views.BandAlbumListAPIView.as_view()

    def test_bandalbum_list_view_should_have_only_instances_from_band(self):
        mommy.make('albums.Album')
        album = mommy.make('albums.Album')

        request = factory.get('/')
        response = self.view(request, pk=album.band.pk).render()
        self.assertEqual(len(response.data), 1)
