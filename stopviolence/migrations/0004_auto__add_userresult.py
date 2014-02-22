# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserResult'
        db.create_table(u'stopviolence_userresult', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('level', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'stopviolence', ['UserResult'])


    def backwards(self, orm):
        # Deleting model 'UserResult'
        db.delete_table(u'stopviolence_userresult')


    models = {
        u'stopviolence.blogentry': {
            'Meta': {'object_name': 'BlogEntry'},
            'dataset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stopviolence.BlogsData']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'stopviolence.blogsdata': {
            'Meta': {'object_name': 'BlogsData'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stopviolence.City']"}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'stopviolence.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'population': ('django.db.models.fields.IntegerField', [], {})
        },
        u'stopviolence.policereport': {
            'Meta': {'object_name': 'PoliceReport'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stopviolence.City']"}),
            'crimes_count': ('django.db.models.fields.IntegerField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'stopviolence.theme': {
            'Meta': {'object_name': 'Theme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'stopviolence.userresult': {
            'Meta': {'object_name': 'UserResult'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.FloatField', [], {}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'stopviolence.violentphoto': {
            'Meta': {'object_name': 'ViolentPhoto'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'phnto_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'theme': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stopviolence.Theme']"}),
            'violent_level': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['stopviolence']