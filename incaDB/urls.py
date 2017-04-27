# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views
from . import funds
from . import prices 

# url order is very important 
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^funds/$', funds.index, name='funds_index'),
	# url(r'^funds/ranks$', funds.rank, name="funds_rank"),
	url(r'^funds/create/$', funds.create, name='funds_create'),
	url(r'^funds/store-single/$', funds.store_single, name='funds_store_single'),
	url(r'^funds/store-multi/$', funds.store_multi, name='funds_store_multi'),
	url(r'^prices/store-multi/$', prices.store_multi, name='price_store_multi'),
	# url(r'^funds/last-prices$', funds.prices_latest, name='funds_prices_latest'),
	# url(r'^funds/(?P<value>.+)/prices$', funds.prices_word, name='funds_prices_word'),
	
	# url(r'^funds/(?P<value>.+)/$', funds.show, name='funds_show'),
]

urlpatterns += static('/upload/', document_root=settings.MEDIA_ROOT)