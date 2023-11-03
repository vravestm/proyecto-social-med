from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')


def contacto(request):
    return render(request, 'core/contacto.html')


def docentes(request):
    return render(request, 'core/docentes.html')


def oferta_formativa(request):
    return render(request, 'core/oferta_formativa.html')
