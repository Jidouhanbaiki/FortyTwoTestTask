# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Other'
        db.delete_table(u'contacts_other')

        # Adding field 'Contact.other_contacts'
        db.add_column(u'contacts_contact', 'other_contacts',
                      self.gf('django.db.models.fields.TextField')(default=' a: b'),
                      keep_default=False)

        # Removing M2M table for field other on 'Contact'
        db.delete_table(db.shorten_name(u'contacts_contact_other'))


    def backwards(self, orm):
        # Adding model 'Other'
        db.create_table(u'contacts_other', (
            ('right', self.gf('django.db.models.fields.CharField')(max_length=48)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('left', self.gf('django.db.models.fields.CharField')(max_length=48)),
        ))
        db.send_create_signal(u'contacts', ['Other'])

        # Deleting field 'Contact.other_contacts'
        db.delete_column(u'contacts_contact', 'other_contacts')

        # Adding M2M table for field other on 'Contact'
        m2m_table_name = db.shorten_name(u'contacts_contact_other')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contact', models.ForeignKey(orm[u'contacts.contact'], null=False)),
            ('other', models.ForeignKey(orm[u'contacts.other'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contact_id', 'other_id'])


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