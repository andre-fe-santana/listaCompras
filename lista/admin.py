from django.contrib import admin
from lista import models

# Register your models here.
@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'imagem', 'data_adicionado', 'prioridade', 'por_que', 'comprado', 'categoria')

@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'icone', 'descricao', 'data_inserido', 'ativo')

@admin.register(models.Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('id', 'loja', 'data', 'link', 'preco', 'item')

