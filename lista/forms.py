from django import forms
from lista.models import Item, Categoria, Historico

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'imagem',
            'nome',
            'categoria',
            'prioridade',
            'por_que',
 
        ]

        widgets = {
            'por_que': forms.Textarea(attrs={'cols': 30, 'rows': 5}), #tava quebrando o CSS
        }

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
            # 'loja',
            'link',
            'preco',
            # 'item', #esse item não vai ser inserido na mesma hora do formulário
        ]