# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Subscription.cancel_word'
        db.delete_column(u'subscriptions_subscription', 'cancel_word_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Subscription.cancel_word'
        raise RuntimeError("Cannot reverse this migration. 'Subscription.cancel_word' and its values cannot be restored.")

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
            'expiration_date': ('django.db.models.fields.DateTimeField', [], {}),
            'facts_sent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interval': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'sub_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['subscriptions']