# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Base'
        db.delete_table(u'worldofe_base')

        # Adding model 'Competition'
        db.create_table(u'worldofe_competition', (
            (u'eitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['worldofe.Eitem'], unique=True, primary_key=True)),
            ('rewards', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'worldofe', ['Competition'])

        # Adding model 'Eitem'
        db.create_table(u'worldofe_eitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['worldofe.Action'])),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'worldofe', ['Eitem'])

        # Adding model 'Employment'
        db.create_table(u'worldofe_employment', (
            (u'eitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['worldofe.Eitem'], unique=True, primary_key=True)),
            ('payment', self.gf('django.db.models.fields.CharField')(default='UN', max_length=2)),
            ('time', self.gf('django.db.models.fields.CharField')(default='SU', max_length=2)),
            ('position', self.gf('django.db.models.fields.CharField')(default='IN', max_length=2)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('deadline', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'worldofe', ['Employment'])

        # Adding model 'Trip'
        db.create_table(u'worldofe_trip', (
            (u'eitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['worldofe.Eitem'], unique=True, primary_key=True)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=2)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('end', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'worldofe', ['Trip'])

        # Adding model 'Workshop'
        db.create_table(u'worldofe_workshop', (
            (u'eitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['worldofe.Eitem'], unique=True, primary_key=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'worldofe', ['Workshop'])

        # Adding model 'Courses'
        db.create_table(u'worldofe_courses', (
            (u'eitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['worldofe.Eitem'], unique=True, primary_key=True)),
            ('dept', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('num', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('professor', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'worldofe', ['Courses'])

        # Adding model 'Action'
        db.create_table(u'worldofe_action', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'worldofe', ['Action'])


    def backwards(self, orm):
        # Adding model 'Base'
        db.create_table(u'worldofe_base', (
            ('text', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('some_more_text', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('moretext', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'worldofe', ['Base'])

        # Deleting model 'Competition'
        db.delete_table(u'worldofe_competition')

        # Deleting model 'Eitem'
        db.delete_table(u'worldofe_eitem')

        # Deleting model 'Employment'
        db.delete_table(u'worldofe_employment')

        # Deleting model 'Trip'
        db.delete_table(u'worldofe_trip')

        # Deleting model 'Workshop'
        db.delete_table(u'worldofe_workshop')

        # Deleting model 'Courses'
        db.delete_table(u'worldofe_courses')

        # Deleting model 'Action'
        db.delete_table(u'worldofe_action')


    models = {
        u'worldofe.action': {
            'Meta': {'object_name': 'Action'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'worldofe.competition': {
            'Meta': {'object_name': 'Competition', '_ormbases': [u'worldofe.Eitem']},
            u'eitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['worldofe.Eitem']", 'unique': 'True', 'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rewards': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'worldofe.courses': {
            'Meta': {'object_name': 'Courses', '_ormbases': [u'worldofe.Eitem']},
            'dept': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'eitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['worldofe.Eitem']", 'unique': 'True', 'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'professor': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'worldofe.eitem': {
            'Meta': {'object_name': 'Eitem'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['worldofe.Action']"}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'worldofe.employment': {
            'Meta': {'object_name': 'Employment', '_ormbases': [u'worldofe.Eitem']},
            'deadline': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'eitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['worldofe.Eitem']", 'unique': 'True', 'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'payment': ('django.db.models.fields.CharField', [], {'default': "'UN'", 'max_length': '2'}),
            'position': ('django.db.models.fields.CharField', [], {'default': "'IN'", 'max_length': '2'}),
            'time': ('django.db.models.fields.CharField', [], {'default': "'SU'", 'max_length': '2'})
        },
        u'worldofe.trip': {
            'Meta': {'object_name': 'Trip', '_ormbases': [u'worldofe.Eitem']},
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '2'}),
            u'eitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['worldofe.Eitem']", 'unique': 'True', 'primary_key': 'True'}),
            'end': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'worldofe.workshop': {
            'Meta': {'object_name': 'Workshop', '_ormbases': [u'worldofe.Eitem']},
            u'eitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['worldofe.Eitem']", 'unique': 'True', 'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['worldofe']