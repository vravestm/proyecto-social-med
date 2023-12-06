from django.shortcuts import render
from .models import Talleres
from django.views.generic import DetailView


def talleres(request):
    if request.user.is_authenticated:
        request.session['usuario']=request.user.id
    tal=Talleres.objects.all()
    return render(request, 'core/talleres.html',{'tal':tal})

class Detalletaller(DetailView):
    model = Talleres
    template_name = 'core/informacion_taller.html'
