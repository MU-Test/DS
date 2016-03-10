from django.contrib import admin
from .models import Cliente, Producto

@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
	list_display = ('nombre', 'telefono', 'direccion_1','foto')

@admin.register(Producto)
class AdminProducto(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'precio','foto', 'proveedor')	