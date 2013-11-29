# coding=utf-8

from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()

    def __unicode__(self):
        return self.name
