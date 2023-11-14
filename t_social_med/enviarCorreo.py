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