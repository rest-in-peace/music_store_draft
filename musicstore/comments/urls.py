# coding: utf-8

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$',
        views.CommentDetailAPIView.as_view(),
        name='comment-detail',
    ),
)
