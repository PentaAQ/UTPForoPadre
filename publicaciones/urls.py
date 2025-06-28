from django.urls import path
from .views import (
    PublicacionesListView,
    ProductDetailView,
    nueva_publicacion,
    MisPublicacionesListView,
    configuracion_cuenta
)

urlpatterns = [
    path('', PublicacionesListView.as_view(), name='home'),
    path('publicacion/nueva/', nueva_publicacion, name='nueva_publicacion'), 
    path('publicacion/<int:pk>/', ProductDetailView.as_view(), name='detalle_publicacion'), 
    path('mis-publicaciones/', MisPublicacionesListView.as_view(), name='mispublicaciones'),
    path('configuracion/', configuracion_cuenta, name='configuracionusuario'),

]
