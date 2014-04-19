# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Base.moretext'
        db.add_column(u'worldofe_base', 'moretext',
                      self.gf('django.db.models.fields.TextField')(default='test'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Base.moretext'
        db.delete_column(u'worldofe_base', 'moretext')


    models = {
        u'worldofe.base': {
            'Meta': {'object_name': 'Base'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moretext': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['worldofe']