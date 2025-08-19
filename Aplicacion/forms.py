from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado, Ruta, Publicacion, Comentario

# Registro
class RegistroUsuarioForms(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")
    class Meta:
        model = UsuarioPersonalizado
        fields = ['username', 'email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'

# Login
class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100, required=True)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=True)

# Crear Rutas
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
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'puntos_interes': forms.Textarea(attrs={'rows': 2}),
        }

# Comunidad
class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['ruta', 'comentario', 'imagen']
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu publicación...'}),
        }

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.TextInput(attrs={'placeholder': 'Añadir un comentario...', 'class': 'comentario-input'}),
        }
