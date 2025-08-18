from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado, Ruta
from .models import Publicacion, Comentario

# ============================
# FORMULARIO DE REGISTRO
# ============================
class RegistroUsuarioForms(UserCreationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'email']  # campos reales del modelo personalizado

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['email'].label = 'Correo electrónico'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'

# ============================
# FORMULARIO DE LOGIN
# ============================
class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

# ============================
# FORMULARIO DE CREACIÓN DE RUTA
# ============================
class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = [
            'nombre_ruta', 'descripcion', 'longitud', 'imagen',
            'dificultad', 'duracion_estimada', 'altitud_maxima', 
            'ubicacion', 'puntos_interes',
            'coordenadas_inicio_lat', 'coordenadas_inicio_lon',
            'coordenadas_fin_lat', 'coordenadas_fin_lon'
        ]

#==================
# COMUNIDAD
#==================
class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['ruta', 'comentario', 'imagen']
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 3}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.TextInput(attrs={'placeholder': 'Añadir un comentario...'}),
        }