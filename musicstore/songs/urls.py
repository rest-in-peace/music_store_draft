# coding: utf-8

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$',
        views.SongListAPIView.as_view(),
        name='song-list',
    ),
    url(r'^(?P<pk>\d+)/$',
        views.SongDetailAPIView.as_view(),
        name='song-detail',
    ),
)
