from django.contrib import admin
from django.urls import path
from core import views as core_views
from cursos import views as cursos_views
from charlas import views as charlas_views
from prevencion import views as prevencion_views

urlpatterns = [
    path('', core_views.home, name='Home'),
    path('contacto/', core_views.contacto, name='contacto'),
    path('docentes/', core_views.docentes, name='docentes'),
    path('cursos/', cursos_views.cursos, name='cursos'),
    path('charlas/', charlas_views.charlas, name='charlas'),
    path('prevencion/', prevencion_views.prevencion, name='prevencion'),
    path('admin/', admin.site.urls),
]
