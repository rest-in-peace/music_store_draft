# coding: utf-8

from django.db import models


class Album(models.Model):
    band = models.ForeignKey('bands.Band', related_name='albums')

    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='covers')

    date_released = models.DateField()

    songs = models.ManyToManyField('songs.Song', through='tracks.Track')

