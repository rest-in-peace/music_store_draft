# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table(u'bands_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('band', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bands.Band'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('release_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'bands', ['Album'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table(u'bands_album')


    models = {
        u'bands.album': {
            'Meta': {'object_name': 'Album'},
            'band': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bands.Band']"}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'release_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'bands.band': {
            'Meta': {'object_name': 'Band'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'bands.song': {
            'Meta': {'object_name': 'Song'},
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['bands']