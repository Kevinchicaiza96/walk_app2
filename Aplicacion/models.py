from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# ===========================
# MODELO PERSONALIZADO DE USUARIO
# ===========================
class UsuarioPersonalizado(AbstractUser):
    def __str__(self):
        return self.username

# ===========================
# MODELO DE RUTA
# ===========================
class Ruta(models.Model):
    nombre_ruta = models.CharField(max_length=255, verbose_name="Nombre de la Ruta")
    vistas = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    imagen = models.ImageField(upload_to='rutas_imagenes/', blank=True, null=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Longitud (km)")

    dificultad_choices = [
        ('FACIL', 'Fácil'),
        ('MODERADO', 'Moderado'),
        ('DIFICIL', 'Difícil'),
        ('EXTREMO', 'Extremo'),
    ]
    dificultad = models.CharField(max_length=50, choices=dificultad_choices, default='MODERADO', verbose_name="Dificultad")

    duracion_estimada = models.CharField(max_length=100, blank=True, null=True, verbose_name="Duración Estimada")
    altitud_maxima = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Altitud Máxima (m)")
    ubicacion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ubicación")
    puntos_interes = models.TextField(blank=True, null=True, verbose_name="Puntos de Interés")

    coordenadas_inicio_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Latitud de Inicio")
    coordenadas_inicio_lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Longitud de Inicio")
    coordenadas_fin_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Latitud de Fin")
    coordenadas_fin_lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Longitud de Fin")

    creada_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='rutas_creadas', verbose_name="Creada por")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    usuarios_favoritos = models.ManyToManyField(settings.AUTH_USER_MODEL, through='UserRutaFavorita', related_name='rutas_favoritas', verbose_name="Marcada como Favorita por")

    class Meta:
        verbose_name = "Ruta"
        verbose_name_plural = "Rutas"
        ordering = ['nombre_ruta']

    def __str__(self):
        return self.nombre_ruta

# ===========================
# MODELO: RUTA FAVORITA
# ===========================
class UserRutaFavorita(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favoritas_intermedias')
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name='favorita_por_usuarios')
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'ruta')
        verbose_name = "Ruta Favorita de Usuario"
        verbose_name_plural = "Rutas Favoritas de Usuarios"

    def __str__(self):
        return f"{self.usuario.username} - {self.ruta.nombre_ruta}"

# ===========================
# MODELO: RUTA RECORRIDA
# ===========================
class RutaRecorrida(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.ruta.nombre_ruta}"

# ===========================
# MODELO COMUNIDAD
# ===========================
class Publicacion(models.Model):
    usuario = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='publicaciones/', blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.ruta.nombre_ruta}"

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE)
    texto = models.TextField(max_length=300)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} comentó en {self.publicacion}"
