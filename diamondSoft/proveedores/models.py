from __future__ import unicode_literals

from django.db import models

class Proveedor(models.Model):
	nombre= models.CharField(max_length=255)
	

	def __str__(self):
		return self.nombre
	class Meta:
		ordering = ('id' , )
