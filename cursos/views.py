from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Cursos
from .models import Inscripcion
from .models import Comentario
from django.contrib.auth.decorators import login_required


def cursos(request):
    if request.user.is_authenticated:
        request.session['usuario']=request.user.id 
    cur=Cursos.objects.all()
    return render(request, 'core/cursos.html',{'cur':cur})


class Detalle(DetailView): #Esta clase permite que se vea el detalle del curso para cada curso
    model = Cursos
    template_name = 'core/informacion_curso.html'

@login_required(login_url='inicio_sesion')
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

class Coment(ListView):
     model = Comentario
     template_name = 'core/comentarios.html'

def enviarcomentario(request):
     
     a = request.GET.get('valor')
     v=[a]

     if request.method == 'POST':
        us = request.POST['usuario'] 
        c = request.POST['cur']
        name = request.POST['nombre']
        cal = request.POST['calific']
        com = request.POST['comentario']
            
        formulario = Comentario(user_id=us,curso_id=c,nombre=name,calificacion=cal,comentario=com)
        formulario.save()
        return redirect('cursos')

     


     return render(request,'core/enviarcomentario.html',{'variable':v})

     



        

