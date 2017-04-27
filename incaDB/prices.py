# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Fund, Price

from datetime import datetime
from datetime import timedelta
from decimal import Decimal

def store_multi(request):
	cnt = 0
	# 5번 파일 읽어서 저장하기 
	if 'file' in request.FILES:
		
		f = request.FILES['file']
		for line in f:
			line_words = line.decode('euc-kr').split(',')
			if 'KLV' in line_words[1]:
				print "---------------------------"
				for i, col in enumerate(line_words):	
					if i ==5:
						print col
				print "---------------------------"

				# 업데이트 
				try:
					price_model = Price.objects.get(fund_FundCode=line_words[1], Tradeday=line_words[0])
					print "model exists"
					cnt = cnt + 1
				# 생성 
				except:
					fund_model = Fund.objects.get(FundCode=line_words[1])
					price_model = Price(
						fund = fund_model,
						Tradeday = line_words[0],
						Price = Decimal(line_words[4]),
						Upndown = Decimal(line_words[5] or 0.0),
					)
					price_model.publish()
					price_model.save() 
					print "price related to the fund save in db"
					
	print cnt 
	
	return HttpResponseRedirect(reverse('funds_index'))

