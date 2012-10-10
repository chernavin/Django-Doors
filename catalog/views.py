#coding=utf-8

from catalog.models import Door, Brand, Color, Size
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
	catalog = Door.objects.all()
	return render_to_response('catalog/index.html',
							  {'catalog': catalog},
							  context_instance = RequestContext(request))

def detail(request, door_id):
	door = get_object_or_404(Door, pk = door_id)
	colors = ', '.join([i.title for i in door.color_set.all()])
	sizes = ', '.join([i.__unicode__() for i in door.size_set.all()])
	return render_to_response('catalog/detail.html',
							  {'door': door,
							   'colors': colors,
							   'sizes': sizes},
							  context_instance = RequestContext(request))

def bybrand(request, brand_id = None):
	if brand_id:
		door_list = Door.objects.filter(brand = brand_id)
		return render_to_response('catalog/bybrandid.html',
								  {'catalog': door_list},
								  context_instance = RequestContext(request))
	else:
		brand_list = Brand.objects.all()
		return render_to_response('catalog/bybrand.html',
								  {'brand_list': brand_list},
								  context_instance = RequestContext(request))

def bycolor(request, color_id = None):
	if color_id:
		door_list = Door.objects.filter(color = color_id)
		return render_to_response('catalog/bycolorid.html',
								  {'catalog': door_list},
								  context_instance = RequestContext(request))
	else:
		color_list = Color.objects.all()
		return render_to_response('catalog/bycolor.html',
								  {'color_list': color_list},
								  context_instance = RequestContext(request))

def bysize(request, size_id = None):
	if size_id:
		door_list = Door.objects.filter(size = size_id)
		return render_to_response('catalog/bysizeid.html',
								  {'catalog': door_list},
								  context_instance = RequestContext(request))
	else:
		size_list = Size.objects.all()
		return render_to_response('catalog/bysize.html',
								  {'size_list': size_list},
								  context_instance = RequestContext(request))