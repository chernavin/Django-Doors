#coding=utf-8

def cart(request):
	cart = request.session.get('cart', '')
	if cart:
		cart = cart.split(',')
	else:
		cart = []
	return {'cart': len(cart)}