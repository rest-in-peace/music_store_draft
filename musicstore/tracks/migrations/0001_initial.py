# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Track'
        db.create_table(u'tracks_track', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['songs.Song'])),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['albums.Album'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('track_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'tracks', ['Track'])

        # Adding unique constraint on 'Track', fields ['song', 'album']
        db.create_unique(u'tracks_track', ['song_id', 'album_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Track', fields ['song', 'album']
        db.delete_unique(u'tracks_track', ['song_id', 'album_id'])

        # Deleting model 'Track'
        db.delete_table(u'tracks_track')


    models = {
        u'albums.album': {
            'Meta': {'object_name': 'Album'},
            'band': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bands.Band']"}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'date_released': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'bands.band': {
            'Meta': {'object_name': 'Band'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'songs.song': {
            'Meta': {'object_name': 'Song'},
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'tracks.track': {
            'Meta': {'unique_together': "(('song', 'album'),)", 'object_name': 'Track'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['albums.Album']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['songs.Song']"}),
            'track_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['tracks']