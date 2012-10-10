from shop.models import Order
from django.contrib import admin

class OrderAdmin(admin.ModelAdmin):
	list_display = ('id' ,'datetime', 'person_name', 'person_phone')
	list_filter = ['datetime']
	date_hierarchy = 'datetime'
	search_fields = ['id']

admin.site.register(Order, OrderAdmin)