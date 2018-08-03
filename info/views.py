from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from .models import Candidato

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def listado(request):
    candidatos = Candidato.objects.all()
    context = { 'candidatos': candidatos }
    return render(request, 'info/index.html', context)

def detalle(request, candidato_id):
    try:
        candidato = Candidato.objects.get(id=candidato_id)
    except Candidato.DoesNotExist:
        raise Http404("Ese candidato no existe")
    return render(request, 'info/detalle.html', {'candidato': candidato})