from django.shortcuts import render, redirect
from .models import Cliente, Producto, Proveedor
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.template import loader
from django.core.urlresolvers import reverse_lazy, reverse
from .forms import  ClienteForm, ProductoForm
from django.contrib import messages

def inicio(request):
	return render(request, "menu.html")

class ClienteUpdate(UpdateView):
    model = Cliente
    fields=('id','nombre', 'telefono', 'direccion_1','foto')
    template_name= 'clientes/editar.html'

    def get_success_url(self):
    	return reverse('appDS:detalle', kwargs={'pk': self.object.pk})	
	

class ListaCliente(ListView):
	model= Cliente
	template_name= 'clientes/cliente_list.html'

	def get_context_data(self, **kwargs):
		context = super(ListaCliente, self).get_context_data(**kwargs)
		context['form'] = ClienteForm
		context['form'].save

		return context


class DetalleCliente(DetailView):
	model = Cliente
	template_name= 'clientes/cliente_detail.html'
	
	def get_context_data(self, **kwargs):
		context= super(DetalleCliente, self).get_context_data(**kwargs)
		context['clientes'] = Cliente.objects.all()
		return context	

       
        
class CrearCliente(CreateView):
	model = Cliente
	fields=('id','nombre', 'telefono', 'direccion_1','foto')
	template_name= 'clientes/cliente_form.html'

	
	def get_context_data(self, **kwargs):
		context= super(CrearCliente, self).get_context_data(**kwargs)

		context['clientes'] = Cliente.objects.all()
		return context

	def get_success_url(self):
    		return reverse('appDS:detalle', kwargs={'pk': self.object.pk})	

	# success_url = reverse_lazy('clientes:clientes')	
    

class BorrarCliente(DeleteView):
	model = Cliente
	field = ('id', 'nombre', 'telefono', 'direccion_1', 'foto')
	template_name='clientes/eliminar.html'
	success_url = reverse_lazy('appDS:agregar')
	

############################ Tabla Producto #################################################################

class AgregarProducto(CreateView):
	model = Producto
	fields=('id','nombre', 'descripcion', 'precio','foto','proveedor')
	template_name= 'productos/producto_form.html'
	mensaje= "Producto agregado!"
	
	def get_context_data(self, **kwargs):
		context= super(AgregarProducto, self).get_context_data(**kwargs)

		context['productos'] = Producto.objects.all()
		return context
	# def post(request):
	# 		if request.POST:
	# 			messages.success(request, 'Producto agregado!!!.')
	# 			return request
	
	# def form_valid(self, form):
	# 	if request.method == 'POST':
	#                 messages.success(request, 'File uploaded!')
		        # return super(AgregarProducto, self).form_valid(form)
	def post(request):
		if request.method == 'POST':
			 if request.session.test_cookie_worked():
			 	# request.session.delete_test_cookie()
			 	return HttpResponse("You're logged in.") 
          
            	
        	
            
    	

    
       

 


 
            
 
            
	    	   
 
        

	def get_success_url(self):
    		return reverse('appDS:detalleProducto', kwargs={'pk': self.object.pk})

   
    
        			


class DetalleProducto(DetailView):
	model = Producto
	template_name= 'productos/producto_detail.html'
	
	def get_context_data(self, **kwargs):
		context= super(DetalleProducto, self).get_context_data(**kwargs)
		context['productos'] = Producto.objects.all()
		return context


class ProductoUpdate(UpdateView):
    model = Producto
    fields=('id','nombre', 'descripcion', 'precio','foto','proveedor') 
	   
    template_name= 'productos/producto_editar.html'

    def get_success_url(self):
    	return reverse('appDS:detalleProducto', kwargs={'pk': self.object.pk})	



class BorrarProducto(DeleteView):
	model = Producto
	fields=('id','nombre', 'descripcion', 'precio','foto','proveedor')
	template_name='productos/producto_eliminar.html'
	success_url = reverse_lazy('appDS:agregarp') 
	
	
		

