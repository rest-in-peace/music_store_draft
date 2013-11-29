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
        mommy.make('bands.Album')
        album = mommy.make('bands.Album')

        request = factory.get('/')
        response = self.view(request, pk=album.band.pk).render()
        self.assertEqual(len(response.data), 1)


class TestSongListView(TestCase):
    def setUp(self):
        mommy.make('bands.Song', name='Yes it is')
        self.view = views.SongListAPIView.as_view()

    def test_song_list_view_should_return_200(self):
        request = factory.get('/')
        response = self.view(request).render()
        self.assertEqual(response.status_code, 200)

    def test_song_list_should_contain_url_to_detail_view(self):
        request = factory.get('/')
        response = self.view(request).render()
        self.assertEqual(response.data[0]['url'], 'http://testserver/songs/1/')


class TestSongDetailView(TestCase):
    def setUp(self):
        mommy.make('bands.Song', name='Yes it is')
        self.view = views.SongDetailAPIView.as_view()

    def test_song_detail_should_return_200(self):
        request = factory.get('/')
        response = self.view(request, pk=1).render()
        self.assertEqual(response.status_code, 200)

    def test_song_detail_shourl_contain_url_to_detail_itself(self):
        request = factory.get('/')
        response = self.view(request, pk=1).render()
        self.assertEqual(response.data['url'], 'http://testserver/songs/1/')
