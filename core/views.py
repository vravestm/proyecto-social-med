from django.shortcuts import render
import time


def home(request):
    var1 = time.time()
    return render(request, 'core/home.html', {'var1': var1})


def contacto(request):
    var1 = time.time()
    return render(request, 'core/contacto.html', {'var1': var1})


def docentes(request):
    var1 = time.time()
    return render(request, 'core/docentes.html', {'var1': var1})


def inicio_sesion(request):
    var1 = time.time()
    return render(request, 'core/inicio_sesion.html', {'var1': var1})


def form_registro(request):
    var1 = time.time()
    return render(request, 'core/form_registro.html', {'var1': var1})
