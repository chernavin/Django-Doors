from django.forms import ModelForm
from catalog.models import Door
from shop.models import Order

class OrderForm(ModelForm):
	class Meta:
		model = Order
		exclude = ['doors']