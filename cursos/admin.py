from django.contrib import admin
from .models import Cursos
from .models import Inscripcion
from .models import Comentario

admin.site.register(Cursos)

class Inscripcionadmin(admin.ModelAdmin):
      list_display = ('curso', 'user','date','id')
      list_filter = ('curso', 'user')
admin.site.register(Inscripcion,Inscripcionadmin)

admin.site.register(Comentario)