from django.shortcuts import render


def cursos(request):
    return render(request, 'core/cursos.html')
