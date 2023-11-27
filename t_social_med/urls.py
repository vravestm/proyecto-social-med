from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from cursos import views as cursos_views
from talleres import views as talleres_views
from prevencion import views as prevencion_views
from django.contrib.auth.views import LoginView, LogoutView

from cursos.views import Detalle

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', core_views.home, name='Home'),
     path('inicio_sesion/', LoginView.as_view(template_name='core/inicio_sesion.html'),
         name='inicio_sesion'),
    path('olvidar_contrasena/', core_views.olvidar_contrasena,
         name='olvidar_contrasena'),
    path('form_registro/', core_views.form_registro, name='form_registro'),
    path('perfil_usuario/', core_views.perfil_usuario, name='perfil_usuario'),
    path('contacto/', core_views.contacto, name='contacto'),
    path('docentes/', core_views.docentes, name='docentes'),
    path('cursos/', cursos_views.cursos),
    path('talleres/', talleres_views.talleres, name='talleres'),
    path('prevencion/', prevencion_views.prevencion, name='prevencion'),
    # path('buscar-cursos/', cursos_views.buscar_cursos, name='buscar_cursos'),
    path('admin/', admin.site.urls),
    path('informacion_curso/<int:pk>/', Detalle.as_view(), name='informacion_curso'), 
    path('confirmacion_curso/',cursos_views.confirmacion,name='confirmacion_curso'),
    path('enviar_correo_contacto/', core_views.enviar_correo_contacto, name='enviar_correo_contacto'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
