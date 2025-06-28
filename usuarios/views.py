from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import UsuarioEditarForm, UsuarioCrearForm

def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'listarusuarios.html', {'usuarios': usuarios})


def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioCrearForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente.')
            return redirect('lista_usuarios')
    else:
        form = UsuarioCrearForm()
    return render(request, 'formusuarios.html', {'form': form, 'accion': 'Crear'})



def editar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UsuarioEditarForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado correctamente.')
            return redirect('lista_usuarios')
    else:
        form = UsuarioEditarForm(instance=usuario)
    return render(request, 'formusuarios.html', {'form': form, 'accion': 'Editar'})


def eliminar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    usuario.delete()
    messages.success(request, 'Usuario eliminado.')
    return redirect('lista_usuarios')

