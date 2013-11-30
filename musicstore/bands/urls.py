# coding: utf-8

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$',
        views.BandListAPIView.as_view(),
        name='band-list',
    ),
    url(r'^(?P<pk>\d+)/$',
        views.BandDetailAPIView.as_view(),
        name='band-detail',
    ),
    url(r'^(?P<pk>\d+)/albums/$',
        views.BandAlbumListAPIView.as_view(),
        name='band-album-list',
    ),
)
