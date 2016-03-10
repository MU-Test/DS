from django.conf.urls import url, include
from django.contrib import admin


from appDS import views

urlpatterns = [
 	# url(r'^', include('appDS.urls', namespace='miApp')),
 	#url(r'^', include('clientes.urls', namespace='clientes')),
 	#url(r'^', include('productos.urls', namespace='productos')),
 	url(r'^', include('appDS.urls', namespace='appDS')),


    url(r'^admin/', admin.site.urls),
]

