#coding=utf=8

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from catalog.models import Door
from shop.models import Order
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from shop.forms import OrderForm

def cart(request):
	cart = request.session.get('cart', '')
	if cart:
		cart = cart.split(',')
	else:
		cart = []

	door_list = Door.objects.filter(id__in = cart)
	return render_to_response('shop/cart.html',
							  {'door_list': door_list},
							  context_instance = RequestContext(request))


def cartadd(request, door_id):
	cart = request.session.get('cart', '')
	if cart:
		cart = cart.split(',')
	else:
		cart = []

	if not door_id in cart:
		cart.append(door_id)
		request.session['cart'] = ','.join(cart)

	return HttpResponseRedirect(reverse('shop-cart'))

def cartdelete(request, door_id):
	cart = request.session.get('cart', '')
	if cart:
		cart = cart.split(',')
	else:
		cart = []

	if door_id in cart:
		cart.remove(door_id)
		request.session['cart'] = ','.join(cart)

	return HttpResponseRedirect(reverse('shop-cart'))

def cartorder(request):
	cart = request.session.get('cart').split(',')

	form = OrderForm(request.POST or None)
	success = None

	if form.is_valid():
		order = form.save(commit = False)
		order.save()

		order.doors = Door.objects.filter(id__in = cart)
		order.save()

		request.session['cart'] = ''
		success = u'Ваш заказ удачно сохранен.'

	return render_to_response('shop/order.html',
							  {'form': form,
							   'success': success},
							  context_instance = RequestContext(request))