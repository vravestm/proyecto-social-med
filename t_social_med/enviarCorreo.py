from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def funcionEnviarCorreo(data:dict):
    subject = data['titulo']
    template =get_template('core/templateCorreo.html')

    content = template.render({
        'prueba':'esto es una prueba',
        'datos':data,
        'token':'asdfg',
    })
    #
    destinatario=list(data['correoDestino'])
    message = EmailMultiAlternatives(subject, '',settings.EMAIL_HOST_USER, destinatario)

    message.attach_alternative(content, 'text/html')
    cantidad_enviados = message.send()
    
    # Validar si el correo fue enviado
    if cantidad_enviados > 0:
        print(f'Correo enviado exitosamente a { destinatario[0]}')
    else:
        print(f'Error al enviar el correo a {destinatario[0]}')

def enviarCorreoContacto(datos_formulario: dict):
    try:
        subject = 'Asunto del Correo' 
        template = get_template('core/enviarCorreoContacto.html') 

        contenido = template.render({
            'datos_formulario': datos_formulario,
        })

        destinatario = 'yenerix.a@gmail.com'  
        message = EmailMultiAlternatives(
            subject=subject,
            body='',  
            from_email=settings.EMAIL_HOST_USER,
            to=[destinatario],
        )
        message.attach_alternative(contenido, 'text/html')
        message.send()

        print(f'Correo enviado exitosamente a {destinatario}')

    except Exception as e:
        print(f'Error al enviar el correo: {str(e)}')
        raise e
    


def funcionRecuperarPassword(data: dict):
    subject = 'Asunto del Correo'
    template = get_template('core/templateCorreo.html')

    content = template.render({
        'prueba': 'esto es una prueba',
        'datos': data,
        'token': 'asdfg',
    })

    destinatario = [data['email']]
    message = EmailMultiAlternatives(subject, '', settings.EMAIL_HOST_USER, destinatario)

    message.attach_alternative(content, 'text/html')
    cantidad_enviados = message.send()

    # Validar si el correo fue enviado
    if cantidad_enviados > 0:
        print(f'Correo enviado exitosamente a {destinatario[0]}')
    else:
        print(f'Error al enviar el correo a {destinatario[0]}')