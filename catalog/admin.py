from catalog.models import Brand, Door, Color, Size
from django.contrib import admin

class ColorInline(admin.TabularInline):
	model = Color
	extra = 3

class SizeInline(admin.TabularInline):
	model = Size
	extra = 3

class DoorAdmin(admin.ModelAdmin):
	inlines = [ColorInline, SizeInline]
	list_display = ('title', 'brand', 'price')
	search_fields = ['title']

admin.site.register(Brand)
admin.site.register(Door, DoorAdmin)