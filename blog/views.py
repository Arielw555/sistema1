from django.http import response
from django.shortcuts import redirect, render
from .models import *
from .forms import PlacasForms
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse




def inicio (request):
    return render (request, 'blog/index.html',{})

def base (request):
    return render(request, 'base.html')  

class CreatePlaca (CreateView):
    model= Placas
    form_class = PlacasForms
    template_name = 'blog/Creador.html'
    success_url = reverse_lazy ('Listado')

def ListPlaca (request) :
    placa=Placas.objects.all()
    return render (request, "blog/Listado.html", {"placas": placa})
    


class UpdatePlaca (UpdateView):
    model= Placas
    form_class = PlacasForms
    template_name = 'blog/Creador.html'
    success_url = reverse_lazy ('Listado')

def DeletePlacas(request,id):
    placa = Placas.objects.get(pk = id)
    placa.delete()
    placa=Placas.objects.all()
    return render(request,'blog/Listado.html',{ "placas": placa, "mensaje":'ok'})
    


