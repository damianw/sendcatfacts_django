from django.db import models

class CancelWord(models.Model):
	word = models.CharField(max_length=20)

class Subscription(models.Model):
  phone = models.CharField(max_length=12)
  facts_sent = models.IntegerField(default=0)
  interval = models.IntegerField(default=10)
  sub_date = models.DateTimeField('date subscribed')
  expiration_date = models.DateTimeField('expiration date')

class Fact(models.Model):
	text = models.CharField(max_length=160)