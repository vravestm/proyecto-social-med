from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
import time

from .forms import UserLoginForm, UserSignUpForm


def login_view(request):
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión correctamente')
            return redirect('Home')
        else:
            messages.warning(
                request, 'Correo electrónico o contraseña invalida')
            return redirect('Home')

    messages.error(request, 'Formulario inválido')
    return redirect('Home')


def signup_view(request):
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
            return redirect('Home')

        except Exception as e:
            print(e)
            return JsonResponse({'detail': f'{e}'})


def logout_view(request):
    logout(request)
    return redirect('Home')


@login_required(login_url='Home')
def profile_view(request):
    return render(request, 'Home')


def perfil_usuario(request):
    var1 = time.time()
    return render(request, 'core/perfil_usuario.html', {'var1': var1})
