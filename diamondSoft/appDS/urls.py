from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    inicio,
    vClientes,
    vProveedores
)

urlpatterns = [
    url(r'^$', inicio, name='portada'),
    url(r'^clientes$', vClientes, name='clientes'),
    url(r'^proveedores$', vProveedores, name='proveedores'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)