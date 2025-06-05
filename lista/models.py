from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=150)
    icone = models.ImageField(upload_to="imagens/icones")
    descricao = models.CharField(max_length=255)
    data_inserido = models.DateField(default=timezone.now)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
# criando as opcoes pro select de prioridade
PRIORIDADE_CHOICES = [
    ('BAIXA', 'Baixa'),
    ('MÉDIA', 'Média'),
    ('Alta', 'Alta'),
]

class Item(models.Model):
    nome = models.CharField(max_length=150)
    imagem = models.ImageField(blank=True, upload_to='imagens/%Y/%m')
    data_adicionado = models.DateField(default=timezone.now)

    prioridade = models.CharField(
        max_length=15,
        choices=PRIORIDADE_CHOICES,
        default='MÉDIA',
        )

    por_que = models.TextField()
    comprado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Historico(models.Model):
    loja = models.CharField(max_length=100)
    data = models.DateField(default=timezone.now)
    link = models.TextField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.loja
