# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RequestLog'
        db.create_table(u'contacts_requestlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('remote_addr', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('http_user_agent', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('time', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'contacts', ['RequestLog'])


    def backwards(self, orm):
        # Deleting model 'RequestLog'
        db.delete_table(u'contacts_requestlog')


    models = {
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '48'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '48'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'skype': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '48'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '48'})
        },
        u'contacts.requestlog': {
            'Meta': {'object_name': 'RequestLog'},
            'http_user_agent': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'remote_addr': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'time': ('django.db.models.fields.FloatField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['contacts']