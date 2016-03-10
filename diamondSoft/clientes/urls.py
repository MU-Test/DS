from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import *


from .views import (
	 inicio,
	 BorrarCliente,
	 ClienteUpdate,
	 CrearCliente,
	 DetalleCliente,
	 ListaCliente,   
)

urlpatterns = [
    url(r'^$', inicio, name='portada'),
    url(r'^clientes/lista$', ListaCliente.as_view(), name='lista'),
	url(r'^cliente/(?P<pk>[0-9]+)/$', DetalleCliente.as_view(), name="detalle"),
	url(r'^clientes/agregar$', CrearCliente.as_view(), name="agregar"),
	url(r'^cliente/(?P<pk>\d+)/eliminar$', BorrarCliente.as_view(template_name="eliminar.html"), name="borrar"),
	url(r'^cliente/(?P<pk>\d+)/actualizar/$', ClienteUpdate.as_view(), name='update'),
   
    #url(r'^proveedores$', vProveedores, name='proveedores'),

] 

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


