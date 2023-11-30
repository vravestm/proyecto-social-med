import time

from django.shortcuts import render
from django.http import HttpResponse
from t_social_med.enviarCorreo import funcionEnviarCorreo, enviarCorreoContacto


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
    request.session['usuarionombre']=request.user.first_name
    request.session['usuarioCorreo']=request.user.email
    var1 = time.time()
    return render(request, 'core/contacto.html', {'var1': var1})


def docentes(request):
    var1 = time.time()
    return render(request, 'core/docentes.html', {'var1': var1})


def olvidar_contrasena(request):
    var1 = time.time()
    return render(request, 'core/olvidar_contrasena.html', {'var1': var1})



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
        return HttpResponse("Correo enviado correctamente. Gracias por contactarnos.")
    else:
        return render(request, 'core/contacto.html')
