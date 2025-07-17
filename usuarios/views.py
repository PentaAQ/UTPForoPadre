from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.contrib import messages
from .forms import UsuarioEditarForm, UsuarioCrearForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
import csv

@login_required
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

@login_required
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

@login_required
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

@login_required
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    messages.success(request, "Usuario eliminado.")
    return redirect("lista_usuarios")
@login_required
def desactivar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if (usuario.is_active == True):
        usuario.is_active = False   
        accion = "desactivado"
    else:
        usuario.is_active = True
        accion = "activado"  
    usuario.save()
    messages.success(request, f"Usuario {accion}.")
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



import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Usuario  # Asegúrate de importar tu modelo

@login_required
def subir_csv(request):
    if request.method == "POST":
        archivo = request.FILES.get("archivo_csv")

        if not archivo or not archivo.name.endswith(".csv"):
            messages.error(request, "El archivo debe ser formato .csv")
            return redirect("subir_csv")

        try:
            datos = archivo.read().decode("utf-8").splitlines()
            reader = csv.DictReader(datos)
            creados = 0
            repetidos = 0
            errores = 0

            for fila in reader:
                try:
                    codigo = fila.get("codigo", "").strip()
                    nombre = fila.get("nombres", "").strip()
                    apellido = fila.get("apellidos", "").strip()
                    correo = fila.get("correo", "").strip()
                    dni = fila.get("dni", "").strip()

                    if not codigo or not correo or not dni:
                        errores += 1
                        continue

                    if Usuario.objects.filter(username=codigo).exists() or Usuario.objects.filter(email=correo).exists():
                        repetidos += 1
                        continue

                    # Crear usuario nuevo
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

                except Exception:
                    errores += 1
                    continue 

            messages.success(
                request,
                f"{creados} usuarios creados. {repetidos} ya existían. {errores} con errores en los datos."
            )

        except Exception as e:
            messages.error(request, f"Error al procesar archivo: {e}")

        return redirect("lista_usuarios")

    return render(request, "subircsv.html")
