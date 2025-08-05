from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado, Ruta, RutaRecorrida, UserRutaFavorita

# ===========================
# ADMIN: USUARIO PERSONALIZADO
# ===========================

@admin.register(UsuarioPersonalizado)
class UsuarioPersonalizadoAdmin(UserAdmin):
    model = UsuarioPersonalizado
    list_display = ('username', 'email', 'is_staff', 'is_active')
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
# ADMIN: OTROS MODELOS
# ===========================

admin.site.register(Ruta)
admin.site.register(UserRutaFavorita)
admin.site.register(RutaRecorrida)
