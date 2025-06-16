<<<<<<< HEAD
from rest_framework.serializers import ModelSerializer, CharField, ReadOnlyField
from core.models import Produto

class ProdutoSerializer(ModelSerializer):
    categoria_nome = CharField(source='categoria.nome', read_only=True)
    fornecedor_nome = CharField(source='fornecedor.nome', read_only=True)
    margem_lucro = ReadOnlyField()
    estoque_baixo = ReadOnlyField()

    class Meta:
        model = Produto
        fields = [
            'id', 'nome', 'descricao', 'codigo_barras',
            'categoria', 'categoria_nome', 'fornecedor', 'fornecedor_nome',
            'preco_custo', 'preco_venda', 'estoque_atual', 'estoque_minimo',
            'margem_lucro', 'estoque_baixo', 'ativo', 'data_criacao'
        ]
=======
from rest_framework.serializers import ModelSerializer

from core.models import Produto


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
>>>>>>> 71aa74115a60bcd504a86ba66b965479b4e1a650
