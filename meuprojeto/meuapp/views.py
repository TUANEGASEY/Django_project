from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    context = {'mensagem': 'Olá do Template Django!'}
    return render(request, 'meuapp/index.html', context)

def sobre(request):
    context = {'mensagem': 'Sobre o Template Django!'}
    return render(request, 'meuapp/sobre.html', context)

def sobreAuthor(request):
    context = {'mensagem': 'Sobre o Autor do Template Django!'}
    return render(request, 'meuapp/sobreAuthor.html', context)
