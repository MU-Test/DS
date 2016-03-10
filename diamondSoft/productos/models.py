from __future__ import unicode_literals
from proveedores.models import Proveedor
from django.db import models

class Producto(models.Model):
	nombre= models.CharField(max_length=255)
	descripcion= models.TextField(max_length=255)
	precio=models.DecimalField(max_digits=5, decimal_places=2)
	foto=models.ImageField( blank=False)
	proveedor= models.ForeignKey(Proveedor, null=True)

	# def __str__(self):
	# 	return self.nombre
	class Meta:
		ordering = ('id' , )
