from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioEditarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'first_name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'last_name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
            'email': forms.EmailInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
        }



class UsuarioCrearForm(UserCreationForm):
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
        help_text=(
            "Tu contraseña no puede parecerse a tu información personal.<br>"
            "Debe tener al menos 8 caracteres.<br>"
            "No puede ser una contraseña común.<br>"
            "No puede ser completamente numérica."
        )
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
        help_text="Escribe la misma contraseña para confirmarla."
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'border border-gray-300 rounded p-2 w-full'}),
        }

