from django.conf.urls import patterns, include, url

urlpatterns = patterns('shop.views',
	url(r'^cart/$', 'cart', name = 'shop-cart'),
	url(r'^cart/(?P<door_id>\d+)/add/$', 'cartadd', name = 'shop-cart-add'),
	url(r'^cart/(?P<door_id>\d+)/delete/$', 'cartdelete', name = 'shop-cart-delete'),
	url(r'^cart/order/$', 'cartorder', name = 'shop-cart-order'),
)