# coding: utf-8

from django.test import TestCase

from rest_framework.test import APIRequestFactory
from model_mommy import mommy

from comments import views


factory = APIRequestFactory()


class TestCommentDetailView(TestCase):
    def setUp(self):
        album = mommy.make('albums.Album')
        self.comment = mommy.make_recipe(
            'comments.album_comment', object_id=album.pk,
        )
        self.view = views.CommentDetailAPIView.as_view()

    def test_detail_view_should_return_200(self):
        request = factory.get('/')
        response = self.view(request, pk=1).render()
        self.assertEqual(response.status_code, 200)
