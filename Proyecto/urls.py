"""
URL configuration for Proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Aplicacion import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from Aplicacion.models import UsuarioPersonalizado 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicacion.urls')),

    # URL GENERALES
    path('perfil/', views.profile_view, name='perfil'),
    path('', views.mostrarHome, name='home'),
    path('juegos/', views.mostrarJuegos, name='juegos'),
    path('ranking/', views.mostrarRanking, name='ranking'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('comunidad/', views.comunidad_view, name='comunidad'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('buscar/', views.buscar_rutas, name='buscar_rutas'),

    # URL RUTAS ESTÁTICAS
    path('morro/', views.mostrarMorro, name='morro'),
    path('cruces/', views.mostrarCruces, name='cruces'),
    path('torre24/', views.mostrarTorre24, name='torre24'),

    # ACCOUNT - Vistas de login
    path('login/', views.mostrarLogin, name='login'),
    path('login2/', views.mostrarLogin2, name='login2'),
    path('login3/', views.mostrarLogin3, name='login3'),
    path('login5/', views.mostrarLogin5, name='login5'),

    # VIDEOJUEGOS

#============== Trivia ===============
    path('trivia/', views.mostrarVideogames, name='trivia_index'),
    path('trivia/menu/', views.mostrarVideogames11, name='trivia_menu'),
    path('trivia/juego/', views.mostrarVideogames12, name='trivia_juego'),
    path('trivia/final/', views.mostrarVideogames13, name='trivia_final'),
#============== Mapa roto =============
path('mapa_roto/', views.mostrarMapaRoto, name= 'mapa_roto' )
]

# URL panel de administración personalizado
@user_passes_test(lambda u: u.is_superuser)
@login_required
def admin_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'admin/admin_usuarios.html', {'usuarios': usuarios})
