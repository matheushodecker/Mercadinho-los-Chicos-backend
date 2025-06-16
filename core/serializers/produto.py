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
