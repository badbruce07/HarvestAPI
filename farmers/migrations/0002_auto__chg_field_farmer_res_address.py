# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Farmer.res_address'
        db.alter_column(u'farmers_farmer', 'res_address', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Farmer.res_address'
        db.alter_column(u'farmers_farmer', 'res_address', self.gf('django.db.models.fields.TextField')())

    models = {
        u'farmers.farmer': {
            'Meta': {'ordering': "('reg_date',)", 'object_name': 'Farmer'},
            'agri_activity': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'alias': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'cell_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateTimeField', [], {}),
            'farmer_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'farmer_idx': ('django.db.models.fields.IntegerField', [], {'max_length': '6'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'reg_date': ('django.db.models.fields.DateTimeField', [], {}),
            'res_address': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'tel_number': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'verified_status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '3', 'blank': 'True'})
        }
    }

    complete_apps = ['farmers']