from __future__ import unicode_literals

from django.db import models

class Cliente(models.Model):
	nombre= models.CharField(max_length=255)
	direccion_1= models.TextField(max_length=255)
	telefono=models.IntegerField(unique=True)
	foto=models.ImageField( blank=False)

	# def __str__(self):
	# 	return self.nombre
	class Meta:
		ordering = ('id' , )

class Proveedor(models.Model):
	nombre= models.CharField(max_length=255)
	

	def __str__(self):
		return self.nombre
	class Meta:
		ordering = ('id' , )

class Producto(models.Model):
	nombre= models.CharField(max_length=255)
	descripcion= models.TextField(max_length=255)
	precio=models.DecimalField(max_digits=5, decimal_places=2)
	foto=models.ImageField( blank=False)
	proveedor= models.ForeignKey(Proveedor, null=True)

	# def __str__(self):
	# 	return self.proveedor
	class Meta:
		ordering = ('id' , )
