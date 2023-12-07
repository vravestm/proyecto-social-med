from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Cursos
from .models import Inscripcion
from .models import Comentario
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404


def cursos(request):
    if request.user.is_authenticated:
        request.session['usuario'] = request.user.id
        cur = Cursos.objects.all()

        return render(request, 'core/cursos.html', {'cur': cur})
    else:
        return redirect('inicio_sesion')


class Detalle(DetailView):  # Esta clase permite que se vea el detalle del curso para cada curso
    model = Cursos
    template_name = 'core/informacion_curso.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curso = self.object  # La instancia del curso actual

        # Verificar si el usuario actual está inscrito en este curso
        esta_inscrito = Inscripcion.objects.filter(
            curso=curso, user=self.request.user).exists()

        # Agregar la información al contexto
        context['esta_inscrito'] = esta_inscrito
        return context


@login_required(login_url='inicio_sesion')
def confirmacion(request):  # Confirmacion para inscribirse dentro del curso

    if request.method == 'GET':

        a = request.GET.get('valor')
        v = [a]
        return render(request, 'core/confirmacion_curso.html', {'variable': v})

    if request.method == 'POST':
        print("entre post")
        print(request.POST['valor'])
        us = request.user.id
        c = request.POST['valor']

        # Obtener el curso
        curso = get_object_or_404(Cursos, pk=c)

        # Obtener el usuario actual
        usuario = request.user.id

        # Verificar si el usuario está inscrito en el curso
        esta_inscrito = Inscripcion.objects.filter(
            curso=curso, user=usuario).exists()
        print(esta_inscrito)

        if (esta_inscrito):
            return JsonResponse({"resp": "inscripcion_existe", "mensaje": "Ya te encuentra inscrito."}, status="200")

        formulario = Inscripcion(user_id=us, curso_id=c)
        formulario.save()
        return JsonResponse({"resp": "inscripcion_ok", "mensaje": "Te haz inscrito correctamente."}, status="200")


class Coment(ListView):
    model = Comentario
    template_name = 'core/comentarios.html'


def enviarcomentario(request):

    a = request.GET.get('valor')
    v = [a]

    if request.method == 'POST':
        us = request.POST['usuario']
        c = request.POST['cur']
        name = request.POST['nombre']
        cal = request.POST['calific']
        com = request.POST['comentario']

        formulario = Comentario(user_id=us, curso_id=c,
                                nombre=name, calificacion=cal, comentario=com)
        formulario.save()
        return redirect('cursos')

    return render(request, 'core/enviarcomentario.html', {'variable': v})
