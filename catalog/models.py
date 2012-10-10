#coding=utf-8

from django.db import models

class Brand(models.Model):
	class Meta:
		verbose_name = u'Бренд'
		verbose_name_plural = u'Бренды'

	title = models.CharField(u'Название бренда', max_length = 64)

	def __unicode__(self):
		return self.title

class Door(models.Model):
	class Meta:
		verbose_name = u'Дверь'
		verbose_name_plural = u'Двери'

	brand = models.ForeignKey(Brand, verbose_name = u'Бренд')
	title = models.CharField(u'Название двери', max_length = 64)
	description = models.TextField(u'Описание двери')
	price = models.FloatField(u'Цена')
	photo = models.FileField(u'Фотография', upload_to = 'catalog/')

	def __unicode__(self):
		return self.title

class Color(models.Model):
	class Meta:
		verbose_name = u'Цвет'
		verbose_name_plural = u'Цвета'

	door = models.ForeignKey(Door, verbose_name = u'Дверь')
	title = models.CharField(u'Название цвета', max_length = 64)

	def __unicode__(self):
		return self.title

class Size(models.Model):
	class Meta:
		verbose_name = u'Размер'
		verbose_name_plural = u'Размеры'

	door = models.ForeignKey(Door, verbose_name = u'Дверь')
	width = models.IntegerField(u'Ширина')
	height = models.IntegerField(u'Высота')

	def __unicode__(self):
		return str(self.width) + 'x' + str(self.height)