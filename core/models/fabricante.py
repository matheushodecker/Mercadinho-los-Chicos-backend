from django.db import models


class Fabricante(models.Model):
    """
    Modelo para armazenar os dados dos fabricantes.
    """

    nome = models.CharField(max_length=255, blank=True, null=True, help_text="Nome comercial.")
    cnpj = models.CharField(max_length=18, unique=True, help_text="CNPJ no formato XX.XXX.XXX/XXXX-XX.")
    
    # Endereço
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, help_text="Sigla do estado (SC).")
    cep = models.CharField(max_length=9, help_text="CEP no formato XXXXX-XXX/XXXXX-XXX.")
    
    # Contato
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    nome_contato = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Fabricante"
        verbose_name_plural = "Fabricantes"
        ordering = ['nome']