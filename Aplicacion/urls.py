from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import comunidad_view

urlpatterns = [
    # ============================
    # RUTAS GENERALES
    # ============================
    path('home/', views.mostrarHome, name='home'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('registro/', views.registro_usuario, name='registro'),
    path('activar/<uidb64>/<token>/', views.activar_cuenta, name='activar_cuenta'),
    path('comunidad/', comunidad_view, name='comunidad'),

    # ============================
    # PERFIL DE USUARIO
    # ============================
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),

    # ============================
    # CRUD DE RUTAS (USUARIO)
    # ============================
    path('rutas/', views.lista_rutas, name='rutas'),
    path('rutas/crear/', views.crear_ruta, name='crear_ruta'),
    path('rutas/<int:ruta_id>/', views.detalle_ruta, name='detalle_ruta'),
    path('ruta/eliminar/<int:pk>/', views.eliminar_ruta, name='eliminar_ruta'),
    path('rutas/<int:ruta_id>/favorito/', views.marcar_favorita, name='marcar_favorita'),
    path('rutas/<int:ruta_id>/quitar_favorito/', views.quitar_favorita, name='quitar_favorita'),

    # ============================
    # VISTAS DE ADMINISTRADOR
    # ============================
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('estadisticas/', views.admin_estadisticas, name='admin_estadisticas'),
    path('rutas_admin/', views.admin_rutas, name='admin_rutas'),
    path('reportes/', views.admin_reportes, name='admin_reportes'),
    path('usuarios/', views.admin_usuarios, name='admin_usuarios'),

    # ============================
    # RECUPERACIÓN DE CONTRASEÑA
    # ============================
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='login2/password_reset.html'), name='password_reset'),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='login2/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='login2/password_reset_confirm.html'), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='login2/password_reset_complete.html'), name='password_reset_complete'),
]

# Sirve archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
