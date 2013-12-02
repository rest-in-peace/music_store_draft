# coding: utf-8

from os.path import join, dirname, abspath
from decimal import Decimal

from django.test import TestCase

from rest_framework.test import APIRequestFactory
from rest_framework.reverse import reverse
from model_mommy import mommy

from tracks import views


factory = APIRequestFactory()
MEDIA_PATH = join(dirname(abspath(__file__)), 'media/')


class TestTrackListView(TestCase):
    def setUp(self):
        self.track = mommy.make('tracks.Track', song__name='Beatles')
        self.view = views.TrackListAPIView.as_view()

    def test_list_track_view_should_return_200(self):
        request = factory.get('/')
        response = self.view(request).render()
        self.assertEqual(response.status_code, 200)

    def test_it_should_return_a_list_of_tracks(self):
        request = factory.get('/')
        response = self.view(request).render()
        self.assertEqual(response.data[0]['price'], self.track.price)

    def test_endpoint_should_contain_url_to_detail(self):
        request = factory.get('/')
        response = self.view(request).render()
        self.assertEqual(
            response.data[0]['url'], 'http://testserver/tracks/1/',
        )

    def test_endpoint_should_show_new_tracks(self):
        track2 = mommy.make('tracks.Track')

        request = factory.get('/')
        response = self.view(request).render()
        self.assertEqual(
            response.data[1]['url'], 'http://testserver/tracks/1/',
        )
        self.assertEqual(
            response.data[0]['url'], 'http://testserver/tracks/2/',
        )

    def test_create_track(self):
        album = mommy.make('albums.Album', title='While Album')
        song = mommy.make('songs.Song', name='Dear Prudence')

        album_url = reverse('album-detail', kwargs={'pk': album.pk})
        song_url = reverse('song-detail', kwargs={'pk': song.pk})

        data = {
            'song': song_url, 'album': album_url, 'price': '0.99',
            'track_file': open(join(MEDIA_PATH, 'mock-file.mp3')),
        }
        request = factory.post('/', data=data)
        response = self.view(request).render()
        self.assertEqual(response.status_code, 201)


class TestTrackDetailView(TestCase):
    def setUp(self):
        self.track = mommy.make('tracks.Track', song__name='Beatles')
        self.view = views.TrackDetailAPIView.as_view()

        request = factory.get('/')
        self.response = self.view(request, pk=1).render()

    def test_endpoint_should_return_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_endpoint_should_have_album_url(self):
        self.assertEqual(
            self.response.data['album'], 'http://testserver/albums/1/'
        )

    def test_endpoint_should_have_song_url(self):
        self.assertEqual(
            self.response.data['song'], 'http://testserver/songs/1/'
        )

    def test_endpoint_should_have_was_bought_field(self):
        self.assertEqual(self.response.data['was_bought'], 4)

    def test_endpoint_should_have_was_download_count_field(self):
        self.assertEqual(self.response.data['download_count'], 4)

    def test_update_track(self):
        album_url = reverse('album-detail', kwargs={'pk': self.track.album.pk})
        song_url = reverse('song-detail', kwargs={'pk': self.track.song.pk})

        data = {
            'song': song_url, 'album': album_url, 'price': '1.0',
            'track_file': open(join(MEDIA_PATH, 'mock-file.mp3')),
        }
        request = factory.put('/', data=data)
        response = self.view(request, pk=self.track.pk).render()
        self.assertEqual(response.status_code, 200)
