from django.db import models
from django.utils import timezone
from .categoria import Categoria
from .fornecedor import Fornecedor

class Produto(models.Model):
    """
    Modelo para armazenar os dados dos produtos.
    """
    nome = models.CharField(max_length=200, help_text="Nome do produto.")
    descricao = models.TextField(blank=True, help_text="Descrição do produto.")
    codigo_barras = models.CharField(max_length=50, unique=True, help_text="Código de barras único do produto.")
    codigo_interno = models.CharField(max_length=50, blank=True, help_text="Código interno do produto.")
    
    # Relacionamentos
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, help_text="Categoria do produto.")
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, help_text="Fornecedor do produto.")
    
    # Preços
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço de custo do produto.")
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2, help_text="Preço de venda do produto.")
    margem_lucro_percentual = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Margem de lucro em %.")
    
    # Estoque
    estoque_atual = models.IntegerField(default=0, help_text="Quantidade atual em estoque.")
    estoque_minimo = models.IntegerField(default=5, help_text="Quantidade mínima em estoque.")
    estoque_maximo = models.IntegerField(default=1000, help_text="Quantidade máxima em estoque.")
    
    # Informações adicionais
    unidade_medida = models.CharField(max_length=10, default='UN', help_text="Unidade de medida (UN, KG, L, etc).")
    peso = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True, help_text="Peso do produto em KG.")
    marca = models.CharField(max_length=100, blank=True, help_text="Marca do produto.")
    
    # Controle
    ativo = models.BooleanField(default=True, help_text="Produto ativo.")
    data_criacao = models.DateTimeField(default=timezone.now)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """Calcula a margem de lucro automaticamente."""
        if self.preco_custo and self.preco_venda:
            self.margem_lucro_percentual = ((self.preco_venda - self.preco_custo) / self.preco_custo) * 100
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    @property
    def margem_lucro(self):
        """Calcula a margem de lucro em percentual."""
        if self.preco_custo > 0:
            return ((self.preco_venda - self.preco_custo) / self.preco_custo) * 100
        return 0

    @property
    def estoque_baixo(self):
        """Verifica se o estoque está baixo."""
        return self.estoque_atual <= self.estoque_minimo

    @property
    def valor_estoque(self):
        """Calcula o valor total do estoque."""
        return self.estoque_atual * self.preco_custo

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']
