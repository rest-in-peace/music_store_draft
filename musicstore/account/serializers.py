# coding: utf-8

from django.contrib.auth.models import User

from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email',)

    def save_object(self, obj, **kwargs):
        obj.set_password(obj.password)
        return super(CreateUserSerializer, self).save_object(obj, **kwargs)

    def to_native(self, obj):
        data = super(CreateUserSerializer, self).to_native(obj)
        del data['password']
        return data

