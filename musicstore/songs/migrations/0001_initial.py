# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Song'
        db.create_table(u'songs_song', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('duration', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'songs', ['Song'])


    def backwards(self, orm):
        # Deleting model 'Song'
        db.delete_table(u'songs_song')


    models = {
        u'songs.song': {
            'Meta': {'object_name': 'Song'},
            'duration': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['songs']