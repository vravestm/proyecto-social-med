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
from django.conf import settings
from core.models import Usuarios

from .forms import UserLoginForm, UserSignUpForm


def inicio_sesion(request):
    var1 = time.time()
    return render(request, 'users/inicio_sesion.html', {'var1': var1})


@login_required(login_url='Home')
def perfil_usuario(request):
    request.session['usuarionombre'] = request.user.first_name
    request.session['usuarioap'] = request.user.last_name
    var1 = time.time()

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
       # return redirect('Home', var1=var1, usuario_autenticado=usuario_autenticado)
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
           # return render(request, 'core/informacion_curso.html', {'var1': '1234'})

        else:
            messages.warning(
                request, 'Correo electrónico o contraseña invalida')
            return redirect('inicio_sesion')
    else:
        messages.error(request, 'Formulario invalido')
        print("entre home 1")
        return redirect('Home')


def signup_view(request):
    var1 = time.time()

    if request.method == 'GET':
        print("entre aqui")
        return redirect('form_registro')

    # provincias_file_path = os.path.join(settings.BASE_DIR, 'core',
    #                                     'static', 'data', 'provincias.json')
    # profesiones_file_path = os.path.join(
    #     settings.BASE_DIR, 'core', 'static', 'data', 'profesiones.json')

    # opciones_nacionalidad = [
    #     ('española', 'Española'),
    #     ('extranjera', 'Extranjera'),
    # ]

    # try:
    #     with open(provincias_file_path) as provincias_file:
    #         provincias_data = json.load(provincias_file)
    #     print(provincias_data)
    # except FileNotFoundError:
    #     print("Archivo 'provincias.json' no encontrado")
    #     provincias_data = []

    # try:
    #     with open(profesiones_file_path) as profesiones_file:
    #         profesiones_data = json.load(profesiones_file)
    #     print(profesiones_data)
    # except FileNotFoundError:
    #     print("Archivo 'profesiones.json' no encontrado")
    #     profesiones_data = []

    # opciones_ciudad = [
    #     (ciudad['code'], ciudad['label']) for ciudad in provincias_data
    # ]

    # opciones_ocupacion = [
    #     (ocupacion['code'], ocupacion['label']) for ocupacion in profesiones_data
    # ]

    # signup_form = UserSignUpForm(request.POST or None)

    # signup_form.fields['nacionalidad'].widget.choices = opciones_nacionalidad
    # signup_form.fields['ciudad'].widget.choices = opciones_ciudad
    # signup_form.fields['ocupacion'].widget.choices = opciones_ocupacion

    # # Agrega las opciones al formulario
    # signup_form.fields['nacionalidad'].widget.choices = [
    #     ('española', 'Española'),
    #     ('extranjera', 'Extranjera'),
    # ]

    # signup_form.fields['ciudad'].widget.choices = [
    #     (ciudad['code'], ciudad['label']) for ciudad in provincias_data
    # ]

    # signup_form.fields['ocupacion'].widget.choices = [
    #     (ocupacion['code'], ocupacion['label']) for ocupacion in profesiones_data
    # ]

    # and signup_form.is_valid()

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
            ciudad = signup_form.cleaned_data.get('ciudad')
            ocupacion = signup_form.cleaned_data.get('ocupacion')

            try:
                user = get_user_model().objects.create(
                    nombre=nombre,
                    apellido=apellido,
                    fecha_nacimiento=fecha_nacimiento,
                    email=email,
                    password=make_password(password),
                    telefono=telefono,
                    nacionalidad=nacionalidad,
                    ciudad=str(ciudad),
                    ocupacion=str(ocupacion),
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
            return HttpResponse("Correo enviado correctamente. Gracias por contactarnos.")
           # return redirect('form_registro')

        # return render(request, 'users/form_registro.html', {
        #     'var1': var1,
        #     'signupForm': signup_form,
        #     'opciones_nacionalidad': opciones_nacionalidad,
        #     'opciones_ciudad': opciones_ciudad,
        #     'opciones_ocupacion': opciones_ocupacion,
        # })


def logout_view(request):
    logout(request)
    return redirect('Home')


# @login_required(login_url='Home')
# def profile_view(request):
#     return render(request, '/perfil_usuario/')
