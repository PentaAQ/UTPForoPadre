from django.contrib import admin
from django.urls import path,include
from .views import logear,cerrar_sesion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', logear, name='logear'),
    path('logout/',cerrar_sesion, name='cerrar_sesion'),
    path('publicacion/', include('publicaciones.urls')),
    path('usuarios/', include('usuarios.urls')),
]
