from django.conf.urls import url, include
from django.contrib import admin


from appDS import views

urlpatterns = [
 	url(r'^', include('appDS.urls', namespace='miApp')),
    url(r'^admin/', admin.site.urls),
]

