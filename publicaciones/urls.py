from django.urls import path
from .views import (
    PublicacionesListView,
    ProductDetailView,
    nueva_publicacion,
    MisPublicacionesListView,
    lista_categorias,
    nueva_categoria,
    editar_categoria,
    eliminar_categoria,
    estadisticas_publicaciones_por_categoria,
    exportar_estadisticas_excel,
)

urlpatterns = [
    path('', PublicacionesListView.as_view(), name='home'),
    path('publicacion/nueva/', nueva_publicacion, name='nueva_publicacion'), 
    path('publicacion/<int:pk>/', ProductDetailView.as_view(), name='detalle_publicacion'), 
    path('mis-publicaciones/', MisPublicacionesListView.as_view(), name='mispublicaciones'),
    path('categorias/', lista_categorias, name='lista_categorias'),
    path('categorias/nueva/', nueva_categoria, name='nueva_categoria'), 
    path('categorias/editar/<int:pk>/', editar_categoria, name='editar_categoria'), 
    path('categorias/eliminar/<int:pk>/', eliminar_categoria, name='eliminar_categoria'),
    path('estadisticas/', estadisticas_publicaciones_por_categoria, name='estadisticas_publicaciones_por_categoria'),
    path('estadisticas/', exportar_estadisticas_excel, name='exportar_estadisticas_excel'),
]
