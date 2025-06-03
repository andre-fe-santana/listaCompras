from django.shortcuts import render, redirect, get_object_or_404
from lista.models import Item, Categoria, Historico
from lista.forms import ItemForm, CategoriaForm, HistoricoForm

# Create your views here.
def mostrarLista(request):
    lista = Item.objects.all()
    categorias = Categoria.objects.all() # para mostrar as opções do usuário

    if request.method == "POST":
        itemForm = ItemForm(request.POST, request.FILES) #item tem imagem
        historicoForm = HistoricoForm(request.POST) 
        print(itemForm.data)
        print(historicoForm.data)

        if not itemForm.is_valid(): # <--- ADICIONE ESTAS DUAS LINHAS
            print("Erros do ItemForm:", itemForm.errors) # <---
        if not historicoForm.is_valid(): # <--- E ESTAS DUAS
            print("Erros do HistoricoForm:", historicoForm.errors) # <---

        if itemForm.is_valid() and historicoForm.is_valid():
            item_obj = itemForm.save()

            #commits separados
            historico = historicoForm.save(commit=False)
            historico.item = item_obj #obj já contém o ID
            historico.save()

            return redirect('/')

    else:
        itemForm = ItemForm()
        historicoForm = HistoricoForm()

    context = {
    'lista': lista, 
    'categorias': categorias,
    'item_form': itemForm,
    'historico_form': historicoForm,
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
