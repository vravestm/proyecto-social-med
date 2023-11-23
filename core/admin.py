from django.contrib import admin
from core.models import Usuarios


admin.site.register(Usuarios)


admin.site.site_header = 'T-Social Med'

admin.site.index_title = 'Panel Administrador'
