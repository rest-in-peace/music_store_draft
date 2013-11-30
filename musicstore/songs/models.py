# coding:utf-8

from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()

    def __unicode__(self):
        return self.name

