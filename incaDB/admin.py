# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Fund, Price

# Register your models here.
# Register your models here.
class FundAdmin(admin.ModelAdmin):
	search_fields = ['FundCode','FundName', 'EstabDay', 'SDAY', 'EDAY', 'CmpCode', 'InvestRegion', 'FundTypeName', 'SalesCode', 'SalesNM', 'MgrName', 'MgrInfo', 'created_date', 'updated_date']

class PriceAdmin(admin.ModelAdmin):
	search_fields = ['Tradeday','Price', 'Upndown', 'created_date', 'updated_date']
	ordering = ('fund', 'Tradeday',)
	
admin.site.register(Fund, FundAdmin)
admin.site.register(Price, PriceAdmin)