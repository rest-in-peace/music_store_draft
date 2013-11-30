# coding: utf-8

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$',
        views.AlbumListAPIView.as_view(),
        name='album-list',
    ),
    url(r'^(?P<pk>\d+)/$',
        views.AlbumRetrieveAPIView.as_view(),
        name='album-detail',
    ),

    url(r'^(?P<pk>\d+)/tracks/$',
        views.AlbumTracksAPIView.as_view(),
        name='album-track-list',
    ),
)
