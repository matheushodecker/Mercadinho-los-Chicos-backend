from django.db import models


from core.models.fornecedor import Fornecedor


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    quantidade_estoque = models.PositiveIntegerField()
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'