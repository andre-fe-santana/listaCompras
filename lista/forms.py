from django import forms
from lista.models import Item, Categoria, Historico

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'imagem',
            'nome',
            'prioridade',
            'por_que',
            'categoria',
        ]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'nome',
            'icone',
            'descricao',
        ]

class HistoricoForm(forms.ModelForm):
    class Meta:
        model = Historico
        fields = [
            'loja',
            'data',
            'link',
            'preco',
            'item',
        ]