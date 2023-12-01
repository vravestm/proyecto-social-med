from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Cursos
from .models import Inscripcion


def cursos(request):
    request.session['usuario']=request.user.id 
    cur=Cursos.objects.all()
    return render(request, 'core/cursos.html',{'cur':cur})


class Detalle(DetailView): #Esta clase permite que se vea el detalle del curso para cada curso
    model = Cursos
    template_name = 'core/informacion_curso.html'


def confirmacion(request): #Confirmacion para inscribirse dentro del curso

    a = request.GET.get('valor')
    v=[a]

    if request.method == 'POST':

            us = request.POST['usuario'] 
            c = request.POST['cur']
            
            formulario = Inscripcion(user_id=us,curso_id=c)
            formulario.save()
            return redirect('Home')
    return render(request,'core/confirmacion_curso.html',{'variable':v})



        

