from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class UsuarioEditarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["username", "dni", "first_name", "last_name", "email"]
        labels = {
            "username": "Nombre de usuario",
            "dni": "DNI",
            "first_name": "Nombre",
            "last_name": "Apellido",
            "email": "Correo electrónico",
        }
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "border border-gray-300 rounded p-2 w-full"}
            ),
            "dni": forms.TextInput(
                attrs={"class": "border border-gray-300 rounded p-2 w-full"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "border border-gray-300 rounded p-2 w-full"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "border border-gray-300 rounded p-2 w-full"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "border border-gray-300 rounded p-2 w-full"}
            ),
        }


class UsuarioCrearForm(UserCreationForm):
    username = forms.CharField(
        label="🎯 Codigo UTP",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-3 py-2 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-4 focus:ring-blue-100 transition-all duration-200 outline-none my-2",
                "placeholder": "Escribe tu codigo.Ejemplo: U12345678",
            }
        ),
        # help_text="Escribe tu codigo.Ejemplo: U12345678",
    )

    dni = forms.RegexField(
        regex=r"^\d{8}$",
        label="🆔 Dni",
        max_length=8,
        min_length=8,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-3 py-2 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-4 focus:ring-blue-100 transition-all duration-200 outline-none my-2",
                'placeholder':"12345678"
            }
        ),
    )
    first_name = forms.CharField(
        label="👤 Nombre",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-3 py-2 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-4 focus:ring-blue-100 transition-all duration-200 outline-none my-2",
                'placeholder':"Tu nombre"
            }
        ),
    )
    last_name = forms.CharField(
        label="👥 Apellido",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-3 py-2 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-4 focus:ring-blue-100 transition-all duration-200 outline-none my-2",
                'placeholder':"Tu apellido"
            }
        ),
    )
    email = forms.EmailField(
        label="📧 Correo electrónico",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "w-full px-3 py-2 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-4 focus:ring-blue-100 transition-all duration-200 outline-none my-2",
                'placeholder':"usuario@ejemplo.com"
            }
        ),
    )
    password1 = forms.CharField(
        label="🔒 Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full px-3 py-2 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-4 focus:ring-blue-100 transition-all duration-200 outline-none my-2",
                'placeholder':"Crea una contraseña segur"
            }
        ),
    )
    password2 = forms.CharField(
        label="✅ Confirmar contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full px-3 py-2 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-4 focus:ring-blue-100 transition-all duration-200 outline-none my-2",
                'placeholder':"Repite tu contraseña"
            }
        ),
        # help_text="Escribe la misma contraseña para confirmarla.",
    )

    class Meta:
        model = Usuario
        fields = [
            "username",
            "dni",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
