# coding: utf-8

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$',
        views.TrackListAPIView.as_view(),
        name='track-list',
    ),
    url(r'^(?P<pk>\d+)/$',
        views.TrackDetailAPIView.as_view(),
        name='track-detail',
    ),
)
