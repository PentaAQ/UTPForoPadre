from django.contrib import admin
from .models import Publicaciones, Comentarios, Categorias
# Register your models here.
admin.site.register(Publicaciones)
admin.site.register(Comentarios)
admin.site.register(Categorias)