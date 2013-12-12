# coding: utf-8

from django.db import models
from django.contrib.auth import get_user_model


class Purchase(models.Model):
    user = models.ForeignKey(get_user_model())
    track = models.ForeignKey('tracks.Track')
