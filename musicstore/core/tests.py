# coding: utf-8

from django.test import TestCase

from rest_framework.test import APIRequestFactory

from core import views


factory = APIRequestFactory()


class TestAPIRoot(TestCase):
    def test_api_root_urls(self):
        request = factory.get('/')
        response = views.api_root(request).render()
        self.assertEqual(
            response.data,
            {
                'bands': 'http://testserver/bands/',
                'albums': 'http://testserver/albums/',
                'songs': 'http://testserver/songs/',
                'users': 'http://testserver/users/',
            }
        )
