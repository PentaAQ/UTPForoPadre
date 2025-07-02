from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioEditarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'dni', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Nombre de usuario',
            'dni': 'DNI',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'dni': forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'first_name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'last_name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'email': forms.EmailInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
        }



class UsuarioCrearForm(UserCreationForm):
    dni = forms.RegexField(
        regex=r'^\d{8}$',
        label='dni',
        max_length=8,
        min_length=8,
        required=True,
        widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'})
    )
    first_name = forms.CharField(
        label='Nombre',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'})
    )
    last_name = forms.CharField(
        label='Apellido',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'})
    )
    email = forms.EmailField(
        label='Correo electrónico',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'})
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
        help_text="Escribe la misma contraseña para confirmarla."
    )

    class Meta:
        model = Usuario
        fields = ['username', 'dni', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
        }

