from django.shortcuts import render


def charlas(request):
    return render(request, 'core/charlas.html')
