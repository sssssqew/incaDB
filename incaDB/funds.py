# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Fund, Price
from django.core import serializers

import csv
import json
import collections

from datetime import datetime
from datetime import timedelta

from django.core.files.base import ContentFile

import os

def save_or_update_model(funds):
	for i, fund in enumerate(funds):
		# 업데이트 
		try:
			fund_model = Fund.objects.get(FundCode=fund)
			print fund
		# 생성 
		except:
			fund_model = Fund(FundCode=fund)
			fund_model.publish()
			fund_model.save() 


# Create your views here.
def create(request):
	return render(request, "incaDB/create.html")

def store_single(request):
	return HttpResponse("store single")

def store_multi(request):
	cnt = 0
	# 1번 파일 읽어서 저장하기 
	if 'file' in request.FILES:
		funds = []
		
		f = request.FILES['file']
		for line in f:
			line_words = line.decode('euc-kr').split(',')
			if 'KLV' in line_words[0]:
				print "---------------------------"
				for i, col in enumerate(line_words):	
					print col
				print "---------------------------"

				# 업데이트 
				try:
					fund_model = Fund.objects.get(FundCode=line_words[0])
					fund_model.FundCode = line_words[0]
					fund_model.FundName = line_words[3]
					fund_model.EstabDay = line_words[4]
					fund_model.SDAY = line_words[5]
					fund_model.EDAY = line_words[6]
					fund_model.CmpCode = line_words[7]
					fund_model.InvestRegion = line_words[8]
					fund_model.FundTypeName = line_words[9]
					fund_model.SalesCode = line_words[10]
					fund_model.SalesNM = line_words[11]
					fund_model.MgrName = line_words[12]
					fund_model.MgrInfo = line_words[13]
					fund_model.change()
					fund_model.save(update_fields=['FundCode', 
						'FundName', 'EstabDay', 'SDAY', 'EDAY', 'CmpCode', 
						'InvestRegion', 'FundTypeName', 'SalesCode', 
						'SalesNM', 'MgrName', 'MgrInfo'])
					
					print "model exists"
				# 생성 
				except:
					fund_model = Fund(
						FundCode = line_words[0], 
						FundName = line_words[3], 
						EstabDay = line_words[4], 
						SDAY = line_words[5], 
						EDAY = line_words[6], 
						CmpCode = line_words[7], 
						InvestRegion = line_words[8], 
						FundTypeName = line_words[9], 
						SalesCode = line_words[10], 
						SalesNM = line_words[11], 
						MgrName = line_words[12], 
						MgrInfo = line_words[13]
					)
					fund_model.publish()
					fund_model.save() 
					cnt = cnt + 1
	print cnt
	# save_or_update_model(funds)

	return HttpResponseRedirect(reverse('funds_index'))


def index(request):
	# word_list = Word.objects.all()
	# query = request.GET.get("search_box")

	# if query:
	# 	word_list = word_list.filter(
	# 		Q(value__icontains=query) |
	# 		Q(donut__icontains=query)
	# 	).distinct()

	# paginator = Paginator(word_list, 6)
	# page = request.GET.get('page')

	# try:
	# 	words = paginator.page(page)
	# except PageNotAnInteger:
	# 	# If page is not an integer, deliver first page.
	# 	words = paginator.page(1)
	# except EmptyPage:
	# 	# If page is out of range (e.g. 9999), deliver last page of results.
	# 	words = paginator.page(paginator.num_pages)

	# context = {'words': words}
	# return render(request, "donutapp/index.html", context)
	return render(request, "incaDB/index.html")