# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'contacts_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('birthdate', self.gf('django.db.models.fields.DateField')()),
            ('other_contacts', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contacts', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'contacts_contact')


    models = {
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '48'})
        }
    }

    complete_apps = ['contacts']