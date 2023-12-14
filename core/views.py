import time

from django.shortcuts import render, redirect
from django.http import HttpResponse
from t_social_med.enviarCorreo import funcionEnviarCorreo, enviarCorreoContacto, funcionRecuperarPassword
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render



def home(request):
    # capturamos la id del usuario que se logee en la pagina
    request.session['usuario'] = request.user.id
    usuario_autenticado = request.user.is_authenticated
    var1 = time.time()

    data = {
        'titulo': 'titulo correo',
        'correoDestino': ['vravest@gmail.com'],
        'curso': 'manejo de la ira',
    }

    return render(request, 'core/home.html', {'var1': var1, 'usuario_autenticado': usuario_autenticado})


def contacto(request):
    if request.user.is_authenticated:
        request.session['usuarionombre'] = request.user.nombre
        request.session['usuarioCorreo'] = request.user.email
    var1 = time.time()
    return render(request, 'core/contacto.html', {'var1': var1})


def docentes(request):
    var1 = time.time()
    return render(request, 'core/docentes.html', {'var1': var1})


def olvidar_contrasena(request):
    if request.method == 'POST':
        destinatario = {
            'email': request.POST.get('ingCorreo', ''),
        }
        funcionRecuperarPassword(destinatario)
        return HttpResponse("Correo enviado.")
    else:
        return render(request, 'core/olvidar_contrasena.html')

    var1 = time.time()
    return render(request, 'core/olvidar_contrasena.html', {'var1': var1})


def recuperar_clave(request):
    var1 = time.time()
    return render(request, 'core/recuperar_clave.html', {'var1': var1})


# def informacion_curso(request):
#     var1 = time.time()
#     return render(request, 'core/informacion_curso.html', {'var1': var1})




def enviar_correo_contacto(request):
    if request.method == 'POST':
        datos_formulario = {
            'nombre': request.POST.get('txtName', ''),
            'email': request.POST.get('txtEmail', ''),
            'mensaje': request.POST.get('txtMsg', ''),
        }
        enviarCorreoContacto(datos_formulario)
        return JsonResponse({'message': 'Correo enviado correctamente. Gracias por contactarnos.'})
    else:
        return render(request, 'core/contacto.html')

    

@login_required
def eliminar_cuenta(request):
    if request.method == 'POST':
        try:
            user = request.user
            user.delete()

            # Envía una respuesta JSON indicando éxito
            return JsonResponse({'title': 'Éxito', 'message': 'Tu cuenta ha sido eliminada exitosamente.', 'icon': 'success'})
        except Exception as e:
            return JsonResponse({'title': 'Error', 'message': f'Ocurrió un error: {str(e)}', 'icon': 'error'})

    return render(request, 'users/eliminar_cuenta.html')


def reportes(request):
    var1 = time.time()
    return render(request, 'core/reportes.html', {'var1': var1})




def aviso_cookies(request):
    var1 = time.time()
    return render(request, 'core/aviso_cookies.html', {'var1': var1})




