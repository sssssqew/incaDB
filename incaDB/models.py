# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Fund(models.Model):
	FundCode = models.CharField(max_length=20,  blank=True, null=True)
	FundName = models.CharField(max_length=100,  blank=True, null=True)
	EstabDay = models.CharField(max_length=8,  blank=True, null=True)   
	SDAY = models.CharField(max_length=8,  blank=True, null=True)  
	EDAY = models.CharField(max_length=8,  blank=True, null=True)
	CmpCode = models.CharField(max_length=10,  blank=True, null=True)
	InvestRegion = models.CharField(max_length=10,  blank=True, null=True)
	FundTypeName = models.CharField(max_length=20,  blank=True, null=True)
	SalesCode = models.CharField(max_length=3,  blank=True, null=True)
	SalesNM = models.CharField(max_length=100,  blank=True, null=True)
	MgrName = models.TextField(blank=True, null=True)
	MgrInfo = models.TextField(blank=True, null=True)
	created_date = models.DateTimeField(blank=True, null=True)
	updated_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.created_date = timezone.now()
		
	def change(self):
		self.updated_date = timezone.now()

	def __str__(self):
		return self.FundName.encode('utf-8')


class Price(models.Model):
	fund = models.ForeignKey(Fund)
	Tradeday = models.CharField(max_length=8,  blank=True, null=True)
	Price = models.DecimalField(max_digits=22, decimal_places=12, blank=True, null=True)
	Upndown = models.DecimalField(max_digits=22, decimal_places=12, blank=True, null=True)
	created_date = models.DateTimeField(blank=True, null=True)
	updated_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.created_date = timezone.now()
		
	def change(self):
		self.updated_date = timezone.now()

	def __str__(self):
		name = self.fund.FundCode + '  ' + self.fund.FundName + '   ' + self.Tradeday
		return name.encode('utf-8')
