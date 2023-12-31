from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Cursos
from .models import Inscripcion
from .models import Comentario
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from t_social_med.enviarCorreo import enviarCorreoConfirmacionInscripcion
# from openpyxl import Workbook


def cursos(request):
    if request.user.is_authenticated:
        request.session['usuario'] = request.user.id
        busqueda = request.POST.get('txt_busqueda', '')
        print(busqueda)
        if busqueda:
            cur = Cursos.objects.filter(
                Q(titulo__icontains=busqueda) | Q(presentacion__icontains=busqueda)
            )
        else:
            # If no search term is provided, get all objects
            cur = Cursos.objects.all()

        return render(request, 'core/cursos.html', {'cur': cur, 'busqueda': busqueda})
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
def confirmacion(request):
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

        # Obtener el correo del usuario
        correo_usuario = request.user.email

        # Luego de guardar la inscripción, enviar el correo de confirmación
        enviarCorreoConfirmacionInscripcion(correo_usuario, curso.titulo, correo_usuario)

        return JsonResponse({"resp": "inscripcion_ok", "mensaje": "Te has inscrito correctamente."}, status="200")


class Coment(ListView):
    model = Comentario
    template_name = 'core/comentarios.html'
    context_object_name = 'comentarios'

    def get_queryset(self):
        return Comentario.objects.all().order_by('-fecha_publicacion')


def enviarcomentario(request):
    a = request.GET.get('valor')
    v = [a]

    if request.method == 'POST':
        us = request.POST['usuario']
        c = request.POST['cur']
        if request.user.is_authenticated:
            name = request.session['nombre'] = request.user.nombre
        cal = request.POST['calific']
        com = request.POST['comentario']

        formulario = Comentario(user_id=us, curso_id=c,
                                nombre=name, calificacion=cal, comentario=com)
        formulario.save()
        return redirect('cursos')

    return render(request, 'core/enviarcomentario.html', {'variable': v})
