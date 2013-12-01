# coding: utf-8

from django.db import models
from django.contrib.contenttypes import generic


class Comment(models.Model):
    content_type = models.ForeignKey('contenttypes.ContentType')
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    text = models.TextField()

    def __unicode__(self):
        return self.text
