from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from cursos import views as cursos_views
from talleres import views as talleres_views
from prevencion import views as prevencion_views
from cursos.views import Detalle
from cursos.views import Coment
from cursos.views import enviarcomentario
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',
         core_views.home, name='Home'),
    path('', include('users.urls', namespace='users')),
    path('olvidar_contrasena/', core_views.olvidar_contrasena,
         name='olvidar_contrasena'),
    path('recuperar_clave/', core_views.recuperar_clave, name='recuperar_clave'),
    path('contacto/', core_views.contacto, name='contacto'),
    path('docentes/', core_views.docentes, name='docentes'),
    path('cursos/', cursos_views.cursos, name='cursos'),
    path('talleres/', talleres_views.talleres, name='talleres'),
    path('prevencion/', prevencion_views.prevencion, name='prevencion'),
    path('informacion_curso/<int:pk>/',Detalle.as_view(), name='informacion_curso'),
    path('confirmacion_curso/', cursos_views.confirmacion,
         name='confirmacion_curso'),
    path('enviar_correo_contacto/', core_views.enviar_correo_contacto,
         name='enviar_correo_contacto'),
    path('inicio_sesion/', users_views.inicio_sesion, name='inicio_sesion'),
    path('form_registro/', users_views.registro, name='form_registro'),
    path('registrar_datos/', users_views.signup_view, name='registrar_datos'),
    path('comentarios/',Coment.as_view(), name='comentarios'),
    path('enviarcomentario/',cursos_views.enviarcomentario,name='enviarcomentario'),
    path('admin/', admin.site.urls),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
