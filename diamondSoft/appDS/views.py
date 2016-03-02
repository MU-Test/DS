from django.shortcuts import render

# Create your views here.
def inicio(request):
	return render(request, "menu.html")

def vClientes(request):
	return render(request, "clientes.html")

def vProveedores(request):
	return render(request, "proveedores.html")