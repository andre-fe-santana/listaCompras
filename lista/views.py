from django.shortcuts import render, redirect, get_object_or_404
from lista.models import Item, Categoria, Historico

# Create your views here.
def mostrarLista(request):
    # colocar o DB depois
    lista = Item.objects.all()

    context = {
        'lista': lista, 
    }

    return render(
        request,
        'lista/index.html',
        context,
    )

def criarItem(request):
    pass

def editarItem(request):
    pass

def deletarItem(request):
    pass
