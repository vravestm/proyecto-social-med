from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
import time
from core.models import Usuarios

from .forms import UserLoginForm, UserSignUpForm


def inicio_sesion(request):
    var1 = time.time()
    return render(request, 'users/inicio_sesion.html', {'var1': var1})


def perfil_usuario(request):
    request.session['usuarionombre']=request.user.first_name
    request.session['usuarioap']=request.user.last_name
    var1 = time.time()
    
    return render(request, 'users/perfil_usuario.html', {'var1': var1})


def registro(request):
    var1 = time.time()
    return render(request, 'users/form_registro.html', {'var1': var1})

def login_view(request):
    login_form = UserLoginForm(request.POST or None)

    if request.method == 'GET':
        print("entre aqui")
        return redirect('inicio_sesion')

    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        print(email)
        user = authenticate(request, email=email, password=password)
        print(user)
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

    if request.method == 'GET':
        print("entre aqui")
        return redirect('form_registro')

    signup_form = UserSignUpForm(request.POST or None)
    if signup_form.is_valid():
        email = signup_form.cleaned_data.get('email')
        first_name = signup_form.cleaned_data.get('first_name')
        last_name = signup_form.cleaned_data.get('last_name')
        password = signup_form.cleaned_data.get('password')
        try:
            user = get_user_model().objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password),
                is_active=True
            )
            login(request, user)
            print("fin logn")
            return redirect(request, 'oferta_formativa.html')

        except Exception as e:
            print(e)
            return JsonResponse({'detail': f'{e}'})

        else:
            # El formulario no es válido, puedes agregar lógica adicional o simplemente redirigir a donde prefieras
            messages.warning(
                request, 'El formulario no es válido. Por favor, corrige los errores.')
            # Redirige a la misma página de registro
            return HttpResponseRedirect(request.path)
    else:
        print("entre home")
        # Si la solicitud no es POST, redirige a la página de inicio o a donde prefieras
        return redirect('Home')


def logout_view(request):
    logout(request)
    return redirect('Home')


@login_required(login_url='Home')
def profile_view(request):
    return render(request, 'Home')
