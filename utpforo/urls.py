from django.contrib import admin
from django.urls import path,include

import usuarios.urls
from . import views
from publicaciones.views import PublicacionesListView
from publicaciones import urls
import usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PublicacionesListView.as_view(), name='home'),
    path('login/', views.logear, name='logear'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('publicacion/', include(urls)),
    path('usuarios/', include(usuarios.urls)),
]
