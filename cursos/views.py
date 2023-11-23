from django.shortcuts import render
from .models import Cursos


def cursos(request):
    cur=Cursos.objects.all()


    return render(request, 'core/cursos.html',{'cur':cur})
