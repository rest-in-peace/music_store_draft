# coding: utf-8

from django.db import models

from songs.models import Song


class Track(models.Model):
    song = models.ForeignKey('songs.Song')
    album = models.ForeignKey('albums.Album', related_name='tracks')

    price = models.DecimalField(max_digits=4, decimal_places=2)

    track_file = models.FileField(upload_to='up/tracks')

    class Meta:
        unique_together = ('song', 'album')
