from django.contrib import admin
from django.urls import path
from core import views as core_views
from cursos import views as cursos_views
from talleres import views as talleres_views
from prevencion import views as prevencion_views

urlpatterns = [
    path('', core_views.home, name='Home'),
    path('inicio_sesion/', core_views.inicio_sesion, name='inicio_sesion'),
    path('form_registro/', core_views.form_registro, name='form_registro'),
    path('contacto/', core_views.contacto, name='contacto'),
    path('docentes/', core_views.docentes, name='docentes'),
    path('cursos/', cursos_views.cursos),
    path('talleres/', talleres_views.talleres, name='talleres'),
    path('prevencion/', prevencion_views.prevencion, name='prevencion'),
    path('admin/', admin.site.urls),
]
