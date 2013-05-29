from django.contrib import admin
from subscriptions.models import Subscription, Fact

class SubscriptionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['phone']}),
		('Interval (minutes)', {'fields': ['interval']}),
		('Date subscribed', {'fields': ['sub_date']}),
		('Expiration date', {'fields': ['expiration_date']}),
	]

class FactAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['text']}),
	]

admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Fact, FactAdmin)