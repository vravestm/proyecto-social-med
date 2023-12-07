from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
import time
import json
import os
from django.contrib.staticfiles import finders
from django.conf import settings
from core.models import Usuarios

from .forms import UserLoginForm, UserSignUpForm


def inicio_sesion(request):
    var1 = time.time()
    return render(request, 'users/inicio_sesion.html', {'var1': var1})


@login_required(login_url='Home')
def perfil_usuario(request):
    var1 = time.time()
    request.session['usuarioNombre'] = request.user.nombre
    request.session['usuarioApellido'] = request.user.apellido
    request.session['usuarioCorreo'] = request.user.email
    request.session['usuarioTelefono'] = request.user.telefono
    request.session['usuarioNacionalidad'] = request.user.nacionalidad
    request.session['usuarioCiudad'] = request.user.ciudad
    request.session['usuarioOcupacion'] = request.user.ocupacion

    return render(request, 'users/perfil_usuario.html', {'var1': var1})


def registro(request):
    var1 = time.time()
    usuario_autenticado = request.user.is_authenticated
    print(usuario_autenticado)
    if usuario_autenticado:

        # Almacena los valores en la sesión
        request.session['var1'] = var1
        request.session['usuario_autenticado'] = usuario_autenticado
        return redirect('Home')

    else:
        return render(request, 'users/form_registro.html', {'var1': var1})


def login_view(request):
    login_form = UserLoginForm(request.POST or None)

    if request.method == 'GET':
        print("entre aqui")
        return redirect('inicio_sesion')

    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        print("fin logn 1")
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente')
            return redirect('cursos')

        else:
            messages.warning(
                request, 'Correo electrónico o contraseña invalida')
            return redirect('inicio_sesion')
    else:
        messages.error(request, 'Formulario invalido')
        print("entre home 1")
        return redirect('Home')


def obtener_label_ciudad(ciudad_code):
    try:

        if ciudad_code == "ninguna":
            return ciudad_code
        # Utiliza finders para encontrar la ruta del archivo en la carpeta static
        file_path = finders.find(f'core/data/provincias.json')
        with open(file_path, 'r') as f:
            ciudades_data = json.load(f)
        for ciudad in ciudades_data:
            if ciudad['code'] == ciudad_code:
                return ciudad['label']
    except FileNotFoundError:
        return None


def obtener_label_ocupacion(ocupacion_code):
    try:
        # Utiliza finders para encontrar la ruta del archivo en la carpeta static
        file_path = finders.find(f'core/data/profesiones.json')
        with open(file_path, 'r') as f:
            ocupaciones_data = json.load(f)
        for ocupacion in ocupaciones_data['ocupaciones']:
            if ocupacion['code'] == ocupacion_code:
                return ocupacion['label']
    except FileNotFoundError:
        return None


def signup_view(request):
    var1 = time.time()

    if request.method == 'GET':
        print("entre aqui")
        return redirect('form_registro')

    if request.method == 'POST':
        signup_form = UserSignUpForm(request.POST or None)

        if signup_form.is_valid():

            nombre = signup_form.cleaned_data.get('nombre')
            apellido = signup_form.cleaned_data.get('apellido')
            fecha_nacimiento = signup_form.cleaned_data.get('fecha_nacimiento')
            email = signup_form.cleaned_data.get('email')
            password = signup_form.cleaned_data.get('password')
            telefono = signup_form.cleaned_data.get('telefono')
            nacionalidad = signup_form.cleaned_data.get('nacionalidad')
            ciudad_code = signup_form.cleaned_data.get('ciudad')
            ocupacion_code = signup_form.cleaned_data.get('ocupacion')

            ciudad_label = obtener_label_ciudad(ciudad_code)
            ocupacion_label = obtener_label_ocupacion(ocupacion_code)

            if ciudad_label is None or ocupacion_label is None:
                return JsonResponse({'detail': 'Error al obtener etiquetas'})

            if nacionalidad == 'extranjera':
                # Si la nacionalidad es extranjera, puedes hacer que el campo ciudad sea opcional
                ciudad = None

            try:
                user = get_user_model().objects.create(
                    nombre=nombre,
                    apellido=apellido,
                    fecha_nacimiento=fecha_nacimiento,
                    email=email,
                    password=make_password(password),
                    telefono=telefono,
                    nacionalidad=nacionalidad,
                    ciudad=ciudad_label,
                    ocupacion=ocupacion_label,
                    is_active=True
                )
                print(user)
                login(request, user)

                return redirect('cursos')

            except Exception as e:
                print(e)
                return JsonResponse({'detail': f'{e}'})
        else:
            print("formulario no valido")
            messages.warning(request, 'formulario no valido')
            return redirect('form_registro')


def logout_view(request):
    logout(request)
    return redirect('Home')


# @login_required(login_url='Home')
# def profile_view(request):
#     return render(request, '/perfil_usuario/')
