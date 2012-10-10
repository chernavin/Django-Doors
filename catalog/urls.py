from django.conf.urls import patterns, include, url

urlpatterns = patterns('catalog.views',
	url(r'^$', 'index', name = 'catalog-index'),

	url(r'^bybrand/$', 'bybrand', name = 'catalog-bybrand'),
	url(r'^bybrand/(?P<brand_id>\d+)/$', 'bybrand', name = 'catalog-bybrand-id'),

	url(r'^bycolor/$', 'bycolor', name = 'catalog-bycolor'),
	url(r'^bycolor/(?P<color_id>\d+)/$', 'bycolor', name = 'catalog-bycolor-id'),

	url(r'^bysize/$', 'bysize', name = 'catalog-bysize'),
	url(r'^bysize/(?P<size_id>\d+)/$', 'bysize', name = 'catalog-bysize-id'),

	url(r'^(?P<door_id>\d+)/$', 'detail', name = 'catalog-detail'),
)