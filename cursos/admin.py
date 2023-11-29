from django.contrib import admin
from .models import Cursos
from .models import Inscripcion

admin.site.register(Cursos)

class Inscripcionadmin(admin.ModelAdmin):
      list_display = ('curso', 'user','date','id')
      list_filter = ('curso', 'user')
admin.site.register(Inscripcion,Inscripcionadmin)