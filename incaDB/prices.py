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
		
		if f.name == 'KFRIN05':
			for line in f:
				line_words = line.decode('euc-kr').split('|')
				if 'KLV' in line_words[1]:
					print "---------------------------"
					for i, col in enumerate(line_words):	
						if i == 1 or i == 3:
							print col
					print "---------------------------"

					# 업데이트 
					try:
						# price_models = Price.objects.filter(Tradeday=line_words[0])
						# for p in price_models:
						# 	p.delete()
						# print "model deleted successfully"
						fund_model = Fund.objects.get(FundCode=line_words[1])
						price_models = Price.objects.get(fund_id=fund_model.id, Tradeday=line_words[0])
						print "price model exists"
						cnt = cnt + 1
					# 생성 
					except:
						try:
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
						# 기준가에 대응되는 펀드가 없는 경우 기준가 정보는 저장하지 않음 
						except:
							print "the fund model related to price dosen't exist in db"

		# print f.name			
		
		else:
			print "file is not allowed" 
			
	print cnt
	
	return HttpResponseRedirect(reverse('funds_index'))

