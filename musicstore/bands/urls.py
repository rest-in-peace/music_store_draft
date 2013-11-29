# coding: utf-8

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^bands/$',
        views.BandListAPIView.as_view(),
        name='band-list',
    ),
    url(r'^bands/(?P<pk>\d+)/$',
        views.BandDetailAPIView.as_view(),
        name='band-detail',
    ),
    url(r'^songs/$',
        views.SongListAPIView.as_view(),
        name='song-list',
    ),
    url(r'^songs/(?P<pk>\d+)/$',
        views.SongDetailAPIView.as_view(),
        name='song-detail',
    ),
)
