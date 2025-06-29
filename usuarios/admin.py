from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'dni', 'first_name', 'last_name', 'email')

admin.site.register(Usuario, UsuarioAdmin)
