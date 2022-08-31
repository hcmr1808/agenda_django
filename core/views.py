from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.

def eventos(request, titulo_evento):
    localiza = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('<h1>{}<h1>'.format(localiza.local))


