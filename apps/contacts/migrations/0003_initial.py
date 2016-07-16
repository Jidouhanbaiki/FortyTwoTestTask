# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Other'
        db.create_table(u'contacts_other', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('left', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('right', self.gf('django.db.models.fields.CharField')(max_length=48)),
        ))
        db.send_create_signal(u'contacts', ['Other'])

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
        ))
        db.send_create_signal(u'contacts', ['Contact'])

        # Adding M2M table for field other on 'Contact'
        m2m_table_name = db.shorten_name(u'contacts_contact_other')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contact', models.ForeignKey(orm[u'contacts.contact'], null=False)),
            ('other', models.ForeignKey(orm[u'contacts.other'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contact_id', 'other_id'])


    def backwards(self, orm):
        # Deleting model 'Other'
        db.delete_table(u'contacts_other')

        # Deleting model 'Contact'
        db.delete_table(u'contacts_contact')

        # Removing M2M table for field other on 'Contact'
        db.delete_table(db.shorten_name(u'contacts_contact_other'))


    models = {
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'other': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['contacts.Other']", 'symmetrical': 'False'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '48'})
        },
        u'contacts.other': {
            'Meta': {'object_name': 'Other'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'right': ('django.db.models.fields.CharField', [], {'max_length': '48'})
        }
    }

    complete_apps = ['contacts']
