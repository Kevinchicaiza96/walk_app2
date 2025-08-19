from django.contrib import admin
from django.urls import path, include
from Aplicacion import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

# ==========================================
# VISTA DE ADMIN PERSONALIZADA
# ==========================================
@user_passes_test(lambda u: u.is_superuser)
@login_required
def admin_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'admin/admin_usuarios.html', {'usuarios': usuarios})

# ==========================================
# URLS PRINCIPALES
# ==========================================
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicacion.urls')),

    # URLs GENERALES
    path('', views.mostrarHome, name='home'),
    path('perfil/', views.profile_view, name='perfil'),
    path('juegos/', views.mostrarJuegos, name='juegos'),
    path('ranking/', views.mostrarRanking, name='ranking'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),  # Login principal
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('comunidad/', views.comunidad_view, name='comunidad'),
    path('buscar/', views.buscar_rutas, name='buscar_rutas'),

    # RUTAS ESTÁTICAS
    path('morro/', views.mostrarMorro, name='morro'),
    path('cruces/', views.mostrarCruces, name='cruces'),
    path('torre24/', views.mostrarTorre24, name='torre24'),

    # LOGIN VARIANTES (si son necesarias)
    path('login2/', views.mostrarLogin2, name='login2'),
    path('login3/', views.mostrarLogin3, name='login3'),
    path('login5/', views.mostrarLogin5, name='login5'),

    # TRIVIA / VIDEOJUEGOS
    path('trivia/', views.mostrarVideogames, name='trivia_index'),
    path('trivia/menu/', views.mostrarVideogames11, name='trivia_menu'),
    path('trivia/juego/', views.mostrarVideogames12, name='trivia_juego'),
    path('trivia/final/', views.mostrarVideogames13, name='trivia_final'),

    # MAPA ROTO
    path('mapa_roto/', views.mostrarMapaRoto, name='mapa_roto'),

    # ADMINISTRACIÓN PERSONALIZADA
    path('admin/usuarios/', admin_usuarios, name='admin_usuarios'),
]
