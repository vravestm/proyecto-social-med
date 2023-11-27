import time

from django.shortcuts import render
from t_social_med.enviarCorreo import funcionEnviarCorreo


def home(request):
    request.session['usuario']=request.user.id #capturamos la id del usuario que se logee en la pagina
    var1 = time.time()

    data = {
        'titulo': 'titulo correo',
        'correoDestino': ['vravest@gmail.com'],
        'curso': 'manejo de la ira',
    }
    # cometnar despues de la prueba
    # funcionEnviarCorreo(data)

    return render(request, 'core/home.html', {'var1': var1})


def contacto(request):
    var1 = time.time()
    return render(request, 'core/contacto.html', {'var1': var1})


def docentes(request):
    var1 = time.time()
    return render(request, 'core/docentes.html', {'var1': var1})


def inicio_sesion(request):
    var1 = time.time()
    return render(request, 'core/inicio_sesion.html', {'var1': var1})


def olvidar_contrasena(request):
    var1 = time.time()
    return render(request, 'core/olvidar_contrasena.html', {'var1': var1})


def form_registro(request):
    var1 = time.time()
    return render(request, 'core/form_registro.html', {'var1': var1})


def perfil_usuario(request):
    var1 = time.time()
    return render(request, 'core/perfil_usuario.html', {'var1': var1})

# def informacion_curso(request):
#     var1 = time.time()
#     return render(request, 'core/informacion_curso.html', {'var1': var1})
