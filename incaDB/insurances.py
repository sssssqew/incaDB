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
	
	return HttpResponse("store insurance mutiple")