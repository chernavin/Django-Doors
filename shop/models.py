#coding=utf-8

from django.db import models
from catalog.models import Door

class Order(models.Model):
	class Meta:
		verbose_name = u'Заказ'
		verbose_name_plural = u'Заказы'

	doors = models.ManyToManyField(Door, verbose_name = u'Двери')
	datetime = models.DateTimeField(u'Дата создания заказа', auto_now_add = True)
	person_name = models.CharField(u'ФИО', max_length = 128)
	person_phone = models.CharField(u'Контактный телефон', max_length = 32)

	def __unicode__(self):
		return u'%s' % self.id