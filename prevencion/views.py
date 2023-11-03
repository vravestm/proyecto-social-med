from django.shortcuts import render


def prevencion(request):
    return render(request, 'core/prevencion.html')
