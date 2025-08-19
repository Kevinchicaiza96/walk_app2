# ===========================
# IMPORTACIONES
# ===========================
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.password_validation import validate_password
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.db.models import Sum
from django.utils.timezone import now, timedelta
from django.db.models import F

from .models import (
    Ruta, UsuarioPersonalizado, UserRutaFavorita, RutaRecorrida,
    Publicacion, Comentario
)
from .forms import (
    RegistroUsuarioForms, LoginForm, RutaForm,
    PublicacionForm, ComentarioForm
)
from .utils import account_activation_token

# ===========================
# HOME Y SECCIONES GENERALES
# ===========================
def mostrarHome(request):
    rutas = Ruta.objects.all()
    dificultad = request.GET.get('dificultad')
    buscar = request.GET.get('buscar')
    distancia_param = request.GET.get('distancia')

    if dificultad:
        rutas = rutas.filter(dificultad__iexact=dificultad)
    if buscar:
        rutas = rutas.filter(nombre_ruta__icontains=buscar)
    if distancia_param:
        try:
            distancia = float(distancia_param)
            rutas = rutas.filter(longitud__lte=distancia)
        except ValueError:
            pass

    return render(request, 'html/home.html', {'rutas': rutas})


def mostrarComunidad(request):
    return render(request, 'html/comunidad.html')


def mostrarRutas(request):
    return render(request, 'html/rutas.html')


def mostrarJuegos(request):
    return render(request, 'html/juegos/juegos.html')


def mostrarRanking(request):
    return render(request, 'html/ranking.html')


# ===========================
# VISTAS INDIVIDUALES DE RUTAS
# ===========================
def mostrarMorro(request):
    return render(request, 'html/rutas/vista-morro.html')


def mostrarCruces(request):
    return render(request, 'html/rutas/vista-tres-cruces.html')


def mostrarTorre24(request):
    return render(request, 'html/rutas/torre_24.html')


# ===========================
# LOGIN Y PERFIL
# ===========================
@login_required
def profile_view(request):
    return render(request, 'html/perfil.html', {
        'nombre_usuario': request.user.username,
        'correo_electronico': request.user.email,
    })


def mostrarLogin(request):
    return render(request, 'login/index.html')


def mostrarLogin2(request):
    return render(request, 'login/mi_perfil.html')


def mostrarLogin3(request):
    return render(request, 'login/recuperar_contrasena.html')


def mostrarLogin5(request):
    return render(request, 'login/restablecer_contrasena.html')


# ===========================
# VIDEOJUEGOS
# ===========================
def mostrarVideogames(request):
    return render(request, 'html/juegos/trivia/index.html')


def mostrarVideogames11(request):
    return render(request, 'html/juegos/trivia/menu.html')


def mostrarVideogames12(request):
    return render(request, 'html/juegos/trivia/juego.html')


def mostrarVideogames13(request):
    return render(request, 'html/juegos/trivia/final.html')


# ===========================
# MAPA ROTO
# ===========================
def mostrarMapaRoto(request):
    return render(request, 'html/juegos/exploracion/mapa_roto.html')


# ===========================
# REGISTRO DE USUARIO
# ===========================
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Enviar correo de activación
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            activation_link = f"http://localhost:8000/activar/{uid}/{token}/"
            message = render_to_string('html/correo_activacion.html', {
                'user': user,
                'activation_link': activation_link
            })
            email_message = EmailMessage(
                subject='Activa tu cuenta en Walk App',
                body=message,
                to=[user.email]
            )
            email_message.content_subtype = "html"
            email_message.send()

            messages.success(request, 'Cuenta creada. Verifica tu correo electrónico.')
            return redirect('login')
        else:
            messages.error(request, 'Revisa los campos del formulario.')
    else:
        form = RegistroUsuarioForms()

    return render(request, 'mi_app_registro/registro.html', {'form': form})


# ===========================
# ACTIVAR CUENTA
# ===========================
def activar_cuenta(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UsuarioPersonalizado.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UsuarioPersonalizado.DoesNotExist):
        user = None

    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, '¡Cuenta activada! Ya puedes iniciar sesión.')
        return redirect('login')
    else:
        messages.error(request, 'El enlace de activación no es válido.')
        return redirect('registro')


# ===========================
# LOGIN Y LOGOUT
# ===========================
def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'¡Bienvenido de nuevo, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'mi_app_registro/login.html', {'form': form})


def logout_usuario(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('login')


# ===========================
# VISTAS DE ADMINISTRADOR
# ===========================
@staff_member_required
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')


@staff_member_required
def admin_estadisticas(request):
    User = get_user_model()
    last_7_days = [now().date() - timedelta(days=i) for i in range(6, -1, -1)]
    fechas = [d.strftime("%d/%m") for d in last_7_days]
    usuarios_por_dia = [User.objects.filter(last_login__date=dia).count() for dia in last_7_days]

    rutas_top = Ruta.objects.order_by('-vistas')[:5]
    rutas_nombres = [ruta.nombre_ruta for ruta in rutas_top]
    rutas_vistas = [ruta.vistas for ruta in rutas_top]

    context = {
        'fechas': fechas,
        'usuarios_por_dia': usuarios_por_dia,
        'rutas_nombres': rutas_nombres,
        'rutas_vistas': rutas_vistas,
    }
    return render(request, 'admin/admin_estadisticas.html', context)


@staff_member_required
def admin_rutas(request):
    return render(request, 'admin/admin_rutas.html')


@staff_member_required
def admin_reportes(request):
    return render(request, 'admin/admin_reportes.html')


@user_passes_test(lambda u: u.is_superuser)
@login_required
def admin_usuarios(request):
    usuarios = UsuarioPersonalizado.objects.all().order_by('-date_joined')
    return render(request, 'admin/admin_usuarios.html', {'usuarios': usuarios})


# ===========================
# PERFIL USUARIO
# ===========================
@login_required
def perfil_usuario(request):
    usuario = request.user
    rutas_recorridas = RutaRecorrida.objects.filter(usuario=usuario)
    total_km = rutas_recorridas.aggregate(total=Sum('ruta__longitud'))['total'] or 0
    total_horas = rutas_recorridas.count() * 3
    rutas_favoritas = usuario.rutas_favoritas.all()

    context = {
        'usuario': usuario,
        'rutas_recorridas': rutas_recorridas,
        'total_km': total_km,
        'total_horas': total_horas,
        'rutas_favoritas': rutas_favoritas,
    }
    return render(request, 'html/perfil_usuario.html', context)


# ===========================
# CRUD RUTAS
# ===========================
def lista_rutas(request):
    rutas = Ruta.objects.all().order_by('nombre_ruta')
    return render(request, 'html/rutas.html', {'rutas': rutas})


def crear_ruta(request):
    if request.method == 'POST':
        form = RutaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('rutas')
    else:
        form = RutaForm()
    return render(request, 'html/rutas/crear_ruta.html', {'form': form})


@staff_member_required
def eliminar_ruta(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    ruta.delete()
    return redirect('rutas')


# ===========================
# FAVORITOS
# ===========================
@login_required
def marcar_favorita(request, ruta_id):
    ruta = get_object_or_404(Ruta, id=ruta_id)
    UserRutaFavorita.objects.get_or_create(usuario=request.user, ruta=ruta)
    return redirect('detalle_ruta', ruta_id=ruta.id)


@login_required
def quitar_favorita(request, ruta_id):
    ruta = get_object_or_404(Ruta, id=ruta_id)
    UserRutaFavorita.objects.filter(usuario=request.user, ruta=ruta).delete()
    return redirect('detalle_ruta', ruta_id=ruta.id)


# ===========================
# DETALLE RUTA
# ===========================
def detalle_ruta(request, ruta_id):
    ruta = get_object_or_404(Ruta, id=ruta_id)
    es_favorita = False
    if request.user.is_authenticated:
        es_favorita = UserRutaFavorita.objects.filter(usuario=request.user, ruta=ruta).exists()
    return render(request, 'html/rutas/detalle_ruta.html', {
        'ruta': ruta,
        'es_favorita': es_favorita
    })


# ===========================
# COMUNIDAD
# ===========================
def comunidad_view(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_publicacion')
    publicacion_form = PublicacionForm()
    comentario_form = ComentarioForm()

    if request.method == 'POST':
        if 'comentario_submit' in request.POST:
            texto = request.POST.get("texto")
            publicacion_id = request.POST.get("publicacion_id")
            if texto and publicacion_id:
                Comentario.objects.create(
                    usuario=request.user,
                    publicacion_id=int(publicacion_id),
                    texto=texto
                )
                messages.success(request, "Comentario agregado con éxito.")
                return redirect("comunidad")
            else:
                messages.error(request, "El comentario no puede estar vacío.")
        else:
            publicacion_form = PublicacionForm(request.POST, request.FILES)
            if publicacion_form.is_valid():
                publicacion = publicacion_form.save(commit=False)
                publicacion.usuario = request.user
                publicacion.save()
                messages.success(request, "Publicación creada con éxito.")
                return redirect('comunidad')
            else:
                messages.error(request, "Error al crear publicación.")

    context = {
        'publicaciones': publicaciones,
        'publicacion_form': publicacion_form,
        'comentario_form': comentario_form,
    }
    return render(request, 'html/comunidad.html', context)


# ===========================
# BUSCADOR
# ===========================
def buscar_rutas(request):
    query = request.GET.get('q', '').strip()
    if query:
        rutas = Ruta.objects.filter(nombre_ruta__icontains=query)
        if rutas.count() == 1:
            return redirect('detalle_ruta', ruta_id=rutas.first().id)
        elif rutas.exists():
            return render(request, 'html/lista_resultados.html', {'rutas': rutas, 'query': query})
        else:
            return render(request, 'html/sin_resultados.html', {'query': query})
    return redirect('rutas')
