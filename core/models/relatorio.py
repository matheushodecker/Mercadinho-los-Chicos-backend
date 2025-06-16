from django.db import models
from django.utils import timezone
from .user import User

class RelatorioVenda(models.Model):
    """
    Modelo para armazenar relatórios de vendas.
    """
    nome = models.CharField(max_length=255, help_text="Nome do relatório.")
    data_inicio = models.DateField(help_text="Data de início do período.")
    data_fim = models.DateField(help_text="Data de fim do período.")
    total_vendas = models.DecimalField(max_digits=12, decimal_places=2, help_text="Total de vendas.")
    quantidade_vendas = models.IntegerField(help_text="Quantidade de vendas.")
    ticket_medio = models.DecimalField(max_digits=10, decimal_places=2, help_text="Ticket médio.")
    usuario_gerador = models.ForeignKey(User, on_delete=models.PROTECT, help_text="Usuário que gerou o relatório.")
    data_geracao = models.DateTimeField(default=timezone.now)
    observacoes = models.TextField(blank=True, help_text="Observações do relatório.")

    def __str__(self):
        return f"{self.nome} - {self.data_inicio} a {self.data_fim}"

    class Meta:
        verbose_name = "Relatório de Venda"
        verbose_name_plural = "Relatórios de Vendas"
        ordering = ['-data_geracao']

class RelatorioEstoque(models.Model):
    """
    Modelo para armazenar relatórios de estoque.
    """
    nome = models.CharField(max_length=255, help_text="Nome do relatório.")
    total_produtos = models.IntegerField(help_text="Total de produtos.")
    produtos_estoque_baixo = models.IntegerField(help_text="Produtos com estoque baixo.")
    valor_total_estoque = models.DecimalField(max_digits=12, decimal_places=2, help_text="Valor total do estoque.")
    usuario_gerador = models.ForeignKey(User, on_delete=models.PROTECT, help_text="Usuário que gerou o relatório.")
    data_geracao = models.DateTimeField(default=timezone.now)
    observacoes = models.TextField(blank=True, help_text="Observações do relatório.")

    def __str__(self):
        return f"{self.nome} - {self.data_geracao.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = "Relatório de Estoque"
        verbose_name_plural = "Relatórios de Estoque"
        ordering = ['-data_geracao']
