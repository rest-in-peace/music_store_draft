# coding: utf-8

from django.db import models


class Albums(models.Model):
    band = models.ForeignKey('bands.Band')
    
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='covers')

    date_released = models.DateField()

