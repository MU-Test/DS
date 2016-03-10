from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView , DetailView
from .models import Producto
# Create your views here.

class AgregarProducto(CreateView):
	model = Producto
	fields=('id','nombre', 'descripcion', 'precio','foto','proveedor')


	
	def get_context_data(self, **kwargs):
		context= super(AgregarProducto, self).get_context_data(**kwargs)

		context['productos'] = Producto.objects.all()
		return context

	def get_success_url(self):
    		return reverse('productos:detalle', kwargs={'pk': self.object.pk})	

class DetalleProducto(DetailView):
	model = Producto

	
	def get_context_data(self, **kwargs):
		context= super(DetalleProducto, self).get_context_data(**kwargs)
		context['productos'] = Producto.objects.all()
		return context	
