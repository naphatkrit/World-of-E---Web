# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Base'
        db.create_table(u'worldofe_base', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'worldofe', ['Base'])


    def backwards(self, orm):
        # Deleting model 'Base'
        db.delete_table(u'worldofe_base')


    models = {
        u'worldofe.base': {
            'Meta': {'object_name': 'Base'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['worldofe']