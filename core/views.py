import time

from django.shortcuts import render
from django.http import HttpResponse
from t_social_med.enviarCorreo import funcionEnviarCorreo, enviarCorreoContacto, funcionRecuperarPassword
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def home(request):
    request.session['usuario']=request.user.id #capturamos la id del usuario que se logee en la pagina
    usuario_autenticado = request.user.is_authenticated
    var1 = time.time()

    data = {
        'titulo': 'titulo correo',
        'correoDestino': ['vravest@gmail.com'],
        'curso': 'manejo de la ira',
    }
    # cometnar despues de la prueba
    # funcionEnviarCorreo(data)

    return render(request, 'core/home.html', {'var1': var1,'usuario_autenticado':usuario_autenticado})

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

        try:
            enviarCorreoContacto(datos_formulario)
            response_data = {
                'status': 'success',
                'message': 'Correo enviado correctamente. Gracias por contactarnos.',
            }
        except Exception as e:
            response_data = {
                'status': 'error',
                'message': f'Error al enviar el correo: {str(e)}',
            }

        # Devolver la respuesta JSON
        return JsonResponse(response_data)
    else:
        return render(request, 'core/contacto.html')