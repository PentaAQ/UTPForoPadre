from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Publicaciones, Usuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from .forms import ComentarioForm
from django.contrib import messages
from .forms import PublicacionForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
class PublicacionesListView(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    model = Publicaciones
    context_object_name = 'publicaciones'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = 'Publicaciones disponibles'
        return context
    
    
class ProductDetailView(DetailView):
    template_name = 'publicacion.html'
    model = Publicaciones
    context_object_name = 'publicacion'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()  # Formulario vacío para el template
        context['comentarios'] = self.object.comentarios.all()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = self.object
            comentario.autor = request.user
            comentario.save()
            messages.success(request, 'Comentario agregado exitosamente')
            return redirect('detalle_publicacion', pk=self.object.pk)
        else:
            messages.error(request, 'Error al agregar el comentario.')
            return self.render_to_response(self.get_context_data(form=form))

def nueva_publicacion(request):
    form = PublicacionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            messages.success(request, 'Publicación creada exitosamente')
            return redirect('home')
        else:
            messages.error(request, 'Error al crear la publicación. Por favor, revisa los datos ingresados.')
    return render(request, 'nueva_publicacion.html', {'form': form})

    
    
    
class MisPublicacionesListView(LoginRequiredMixin, ListView):
    template_name = 'mispublicaciones.html'
    model = Publicaciones
    context_object_name = 'publicaciones'

    def get_queryset(self):
        return Publicaciones.objects.filter(autor=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = 'Mis publicaciones'
        return context
    
    


@login_required
def configuracion_cuenta(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña actualizada correctamente.')
            return redirect('configuracion_cuenta')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'configuracion.html', {
        'form': form,
        'usuario': request.user
    })


