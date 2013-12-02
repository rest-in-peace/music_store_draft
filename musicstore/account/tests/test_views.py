# coding: utf-8

from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIRequestFactory
from model_mommy import mommy

from account import views


factory = APIRequestFactory()


class TestUserCreateView(TestCase):
    def setUp(self):
        self.view = views.UserCreateAPIView.as_view()
        self.data = {
            'username': 'elvis', 'email': 'elvis@x.com',
            'password': '123',
        }
        request = factory.post('/', data=self.data, format='json')
        self.response = self.view(request).render()

    def test_post_should_return_201(self):
        self.assertEqual(self.response.status_code, 201)

    def test_password_should_be_set_in_correct_format(self):
        self.assertNotEqual(User.objects.get().password, '123')

    def test_password_should_not_be_on_response(self):
        self.assertNotIn('password', self.response.data)
