# coding: utf-8

from django.conf.urls import patterns, url


from . import views


urlpatterns = patterns('',
    url(r'^track/(?P<pk>\d+)/$', 
        views.TrackPurchaseView.as_view(),
        name='purchase-track'
    )
)
