from django.shortcuts import render, redirect
from .models import Cliente
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Cliente
#from .forms import ClienteForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView , DeleteView
from .forms import  ClienteForm
def inicio(request):
	return render(request, "menu.html")

class ClienteUpdate(UpdateView):
    model = Cliente
    fields=('id','nombre', 'telefono', 'direccion_1','foto')
    template_name= 'clientes/editar.html'

    def get_success_url(self):
    	return reverse('clientes:detalle', kwargs={'pk': self.object.pk})	
	

class ListaCliente(ListView):
	model= Cliente

	def get_context_data(self, **kwargs):
		context = super(ListaCliente, self).get_context_data(**kwargs)
		context['form'] = ClienteForm
		context['form'].save

		return context


class DetalleCliente(DetailView):
	model = Cliente

	
	def get_context_data(self, **kwargs):
		context= super(DetalleCliente, self).get_context_data(**kwargs)
		context['clientes'] = Cliente.objects.all()
		return context	

       
        
class CrearCliente(CreateView):
	model = Cliente
	fields=('id','nombre', 'telefono', 'direccion_1','foto')

	
	def get_context_data(self, **kwargs):
		context= super(CrearCliente, self).get_context_data(**kwargs)

		context['clientes'] = Cliente.objects.all()
		return context

	def get_success_url(self):
    		return reverse('clientes:detalle', kwargs={'pk': self.object.pk})	

	# success_url = reverse_lazy('clientes:clientes')	
    

class BorrarCliente(DeleteView):
	model = Cliente
	field = ('id', 'nombre', 'telefono', 'direccion_1', 'foto')
	template_name='clientes/eliminar.html'
	success_url = reverse_lazy('clientes:agregar')
	
# def borrar_cliente(request, id):
# 	cliente = Cliente.objects.get(id=id)
# 	cliente.delete()
# 	success_message = "Se borro"	
# 	return HttpResponseRedirect('/',success_message)		 			