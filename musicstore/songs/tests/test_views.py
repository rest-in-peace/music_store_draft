# coding: utf-8

from django.test import TestCase

from rest_framework.test import APIRequestFactory
from model_mommy import mommy

from songs import views


factory = APIRequestFactory()


class TestSongListView(TestCase):
    def setUp(self):
        mommy.make('songs.Song', name='Yes it is')
        self.view = views.SongListAPIView.as_view()

    def test_song_list_view_should_return_200(self):
        request = factory.get('/')
        response = self.view(request).render()
        self.assertEqual(response.status_code, 200)

    def test_song_list_should_contain_url_to_detail_view(self):
        request = factory.get('/')
        response = self.view(request).render()
        self.assertEqual(response.data[0]['url'], 'http://testserver/songs/1/')

    def test_create_song(self):
        data = {'name': 'Michelle', 'duration': 100}
        request = factory.post('/', data=data, format='json')
        response = self.view(request).render()
        self.assertEqual(response.status_code, 201)



class TestSongDetailView(TestCase):
    def setUp(self):
        mommy.make('songs.Song', name='Yes it is')
        self.view = views.SongDetailAPIView.as_view()

    def test_song_detail_should_return_200(self):
        request = factory.get('/')
        response = self.view(request, pk=1).render()
        self.assertEqual(response.status_code, 200)

    def test_song_detail_shourl_contain_url_to_detail_itself(self):
        request = factory.get('/')
        response = self.view(request, pk=1).render()
        self.assertEqual(response.data['url'], 'http://testserver/songs/1/')
