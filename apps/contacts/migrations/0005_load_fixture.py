# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.core.management import call_command

class Migration(DataMigration):

    def forwards(self, orm):
        call_command("loaddata", "data2.json")

    def backwards(self, orm):
        "Write your backwards methods here."

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
    symmetrical = True
