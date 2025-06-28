from .models import Publicaciones, Comentarios, Categorias
from django import forms

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['titulo', 'contenido', 'categoria']
        labels = {
            'titulo': 'Título',
            'contenido': 'Contenido',
            'categoria': 'Categoría',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full',
                'placeholder': 'Ingrese el título de la publicación'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full',
                'placeholder': 'Ingrese el contenido de la publicación'
            }),
            'categoria': forms.Select(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full'
            }),
        }

        

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'border border-gray-300 rounded p-2 w-full',
                'placeholder': 'Escribe tu comentario aquí...'
            }),
        }
        labels = {
            'contenido': ''
        }