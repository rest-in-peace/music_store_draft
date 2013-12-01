from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^bands/', include('bands.urls')),
    url(r'^albums/', include('albums.urls')),
    url(r'^songs/', include('songs.urls')),
    url(r'^comments/', include('comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
