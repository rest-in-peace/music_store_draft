
from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APIRequestFactory, APIClient
from model_mommy import mommy

from albums import views


factory = APIRequestFactory()
client = APIClient()

class TestAlbumListView(TestCase):

    def setUp(self):
        self.album = mommy.make('albums.Album', title='White Album')
        self.view = views.AlbumListAPIView.as_view()
        self.url = reverse('albums:album-list')

        request = factory.get('/')
        self.response = self.view(request).render()

    def test_view_url(self):
        url = self.url
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_albums_list_view_should_return_200(self):
        response = self.response
        self.assertEqual(response.status_code, 200)

    def test_should_return_a_list_of_albums(self):
        response = self.response
        album = self.album

        self.assertEquals(type(response.data), list)

        self.assertEquals(response.data[0]['title'], album.title)


class TestAlbumDetailView(TestCase):

    def setUp(self):
        self.album = mommy.make('albums.Album', title='White Album')
        self.view = views.AlbumRetrieveAPIView.as_view()
        self.url = reverse('albums:album-detail', kwargs={'pk': self.album.pk})

        request = factory.get('/')
        self.response = self.view(request, pk=self.album.pk).render()

    def test_should_return_200(self):
        response = self.response
        self.assertEqual(response.status_code, 200)

    def test_view_url(self):
        url = self.url
        response = client.get(url)

        self.assertEqual(response.status_code, 200)


