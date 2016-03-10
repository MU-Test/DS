from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class AdminCliente(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion', 'precio','foto', 'proveedor')