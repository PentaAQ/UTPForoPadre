from .models import Publicaciones, Comentarios, Categorias
from django import forms

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields = ['titulo', 'contenido', 'categoria']
        labels = {
            'titulo': '🎯 Título de la Publicación',
            'contenido': '📄 Contenido',
            'categoria': '🏷️ Categoría',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border-2 border-gray-300 rounded-xl focus:border-blue-500 focus:ring-4 focus:ring-blue-100 transition-all duration-200 outline-none text-lg font-medium my-2 focus:bg-white',
                'placeholder': 'Escribe un título atractivo y descriptivo...'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border-2 border-gray-300 rounded-xl focus:border-blue-500 focus:ring-4 focus:ring-blue-100 transition-all duration-200 outline-none text-md my-2 focus:bg-white',
                'placeholder': 'Ingrese el contenido de la publicación'
            }),
            'categoria': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border-2 border-gray-300 rounded-xl focus:border-blue-500 focus:ring-4 focus:ring-blue-100 transition-all duration-200 outline-none text-md  my-2 focus:bg-white'                
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

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['nombre']
        labels = {
            'nombre': 'nombre',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full',
                'placeholder': 'Ingrese el nombre de la categoría'
            }),
        }
