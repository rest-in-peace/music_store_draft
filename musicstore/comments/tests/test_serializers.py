# coding: utf-8

from django.test import TestCase

from model_mommy import mommy

from comments.serializers import CommentSerializer


class TestCommentSerializer(TestCase):
    def setUp(self):
        album = mommy.make('albums.Album')
        self.comment = mommy.make_recipe(
            'comments.album_comment', object_id=album.pk,
        )

    def test_serializer_should_not_have_content_type(self):
        ser = CommentSerializer(self.comment)
        self.assertNotIn('content_type', ser.data)

    def test_serializer_should_not_have_object_id(self):
        ser = CommentSerializer(self.comment)
        self.assertNotIn('object_id', ser.data)

    def test_serializer_should_have_url_field(self):
        ser = CommentSerializer(self.comment)
        self.assertEqual(ser.data['url'], '/comments/1/')
