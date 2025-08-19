from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado, Ruta, RutaRecorrida, UserRutaFavorita

# ===========================
# ADMIN: USUARIO PERSONALIZADO
# ===========================
@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(UserAdmin):
    model = UsuarioPersonalizado
    list_display = ('username', 'email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('id',)

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Permisos", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Fechas importantes", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "is_staff", "is_active")}
        ),
    )

# ===========================
# ADMIN: RUTA
# ===========================
@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('nombre_ruta', 'vistas', 'dificultad', 'longitud', 'creada_por', 'fecha_creacion')
    list_filter = ('dificultad',)
    search_fields = ('nombre_ruta', 'descripcion', 'ubicacion')

# ===========================
# ADMIN: RUTA FAVORITA
# ===========================
@admin.register(UserRutaFavorita)
class UserRutaFavoritaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'ruta', 'fecha_agregado')
    search_fields = ('usuario__username', 'ruta__nombre_ruta')

# ===========================
# ADMIN: RUTA RECORRIDA
# ===========================
@admin.register(RutaRecorrida)
class RutaRecorridaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'ruta', 'fecha')
    search_fields = ('usuario__username', 'ruta__nombre_ruta')
