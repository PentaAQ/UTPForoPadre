from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.contrib import messages
from .forms import UsuarioEditarForm, UsuarioCrearForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
import csv


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    usuarios_activos = usuarios.filter(is_active=True).count()
    usuarios_inactivos = usuarios.filter(is_active=False).count()
    usuarios_staff = usuarios.filter(is_staff=True).count()
    return render(
        request,
        "listarusuarios.html",
        {
            "usuarios": usuarios,
            "usuarios_activos": usuarios_activos,
            "usuarios_inactivos": usuarios_inactivos,
            "usuarios_staff": usuarios_staff,
        },
    )


def crear_usuario(request):
    if request.method == "POST":
        form = UsuarioCrearForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado correctamente.")
            return redirect("lista_usuarios")
    else:
        form = UsuarioCrearForm()
    return render(request, "formusuarios.html", {"form": form, "accion": "Crear"})


def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioEditarForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario actualizado correctamente.")
            return redirect("lista_usuarios")
    else:
        form = UsuarioEditarForm(instance=usuario)
    return render(request, "formusuarios.html", {"form": form, "accion": "Editar"})


def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    messages.success(request, "Usuario eliminado.")
    return redirect("lista_usuarios")

@login_required
def configuracion_cuenta(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Contraseña actualizada correctamente.")
            return redirect("configuracion_cuenta")
        else:
            messages.error(request, "Por favor corrige los errores.")
    else:
        form = PasswordChangeForm(user=request.user)

    return render(
        request, "configuracion.html", {"form": form, "usuario": request.user}
    )




def subir_csv(request):
    if request.method == "POST":
        archivo = request.FILES.get("archivo_csv")

        if not archivo.name.endswith(".csv"):
            messages.error(request, "El archivo debe ser formato .csv")
            return redirect("subir_csv")

        try:
            datos = archivo.read().decode("utf-8").splitlines()
            reader = csv.DictReader(datos)
            creados = 0
            repetidos = 0

            for fila in reader:
                codigo = fila["codigo"].strip()
                nombre = fila["nombres"].strip()
                apellido = fila["apellidos"].strip()
                correo = fila["correo"].strip()
                dni = fila["dni"].strip()

                if (
                    Usuario.objects.filter(username=codigo).exists()
                    or Usuario.objects.filter(email=correo).exists()
                ):
                    repetidos += 1
                    continue

                usuario = Usuario.objects.create_user(
                    username=codigo,
                    dni=dni,
                    first_name=nombre,
                    last_name=apellido,
                    email=correo,
                    password=dni,
                )
                usuario.is_active = True
                usuario.save()
                creados += 1

            messages.success(
                request, f"{creados} usuarios creados. {repetidos} ya existían."
            )

        except Exception as e:
            messages.error(request, f"Error al procesar archivo: {e}")

        return redirect("subir_csv")

    return render(request, "subircsv.html")
