# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CancelWord'
        db.create_table(u'subscriptions_cancelword', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('word', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'subscriptions', ['CancelWord'])

        # Adding model 'Subscription'
        db.create_table(u'subscriptions_subscription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('facts_sent', self.gf('django.db.models.fields.IntegerField')()),
            ('interval', self.gf('django.db.models.fields.IntegerField')()),
            ('cancel_word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['subscriptions.CancelWord'])),
            ('sub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('expiration_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'subscriptions', ['Subscription'])

        # Adding model 'Fact'
        db.create_table(u'subscriptions_fact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=160)),
        ))
        db.send_create_signal(u'subscriptions', ['Fact'])


    def backwards(self, orm):
        # Deleting model 'CancelWord'
        db.delete_table(u'subscriptions_cancelword')

        # Deleting model 'Subscription'
        db.delete_table(u'subscriptions_subscription')

        # Deleting model 'Fact'
        db.delete_table(u'subscriptions_fact')


    models = {
        u'subscriptions.cancelword': {
            'Meta': {'object_name': 'CancelWord'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'subscriptions.fact': {
            'Meta': {'object_name': 'Fact'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'subscriptions.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'cancel_word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['subscriptions.CancelWord']"}),
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {}),
            'facts_sent': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('django.db.models.fields.IntegerField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'sub_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['subscriptions']