from __future__ import unicode_literals

from django.db import models

class Cliente(models.Model):
	nombre= models.CharField(max_length=255)
	direccion_1= models.TextField(max_length=255)
	telefono=models.IntegerField(unique=True)
	foto=models.ImageField( blank=False)

	def __str__(self):
		return self.nombre
	class Meta:
		ordering = ('id' , )
