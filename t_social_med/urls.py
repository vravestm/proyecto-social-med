from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from cursos import views as cursos_views
from talleres import views as talleres_views
from prevencion import views as prevencion_views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', core_views.home, name='Home'),
    path('inicio_sesion/', core_views.form_registro, name='inicio_sesion'),
    path('olvidar_contrasena/', core_views.olvidar_contrasena,
         name='olvidar_contrasena'),
    path('', include('users.urls', namespace='users')),
    path('form_registro/', core_views.form_registro, name='form_registro'),
    path('perfil_usuario/', core_views.perfil_usuario, name='perfil_usuario'),
    path('contacto/', core_views.contacto, name='contacto'),
    path('docentes/', core_views.docentes, name='docentes'),
    path('oferta_formativa/', core_views.oferta_formativa, name='oferta_formativa'),
    path('cursos/', cursos_views.cursos),
    path('talleres/', talleres_views.talleres, name='talleres'),
    path('prevencion/', prevencion_views.prevencion, name='prevencion'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('informacion_curso/', core_views.informacion_curso,
         name='informacion_curso'),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
