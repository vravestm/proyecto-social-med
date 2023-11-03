from django.shortcuts import render


def talleres(request):
    return render(request, 'core/talleres.html')
