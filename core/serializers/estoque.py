from rest_framework.serializers import ModelSerializer, CharField, ReadOnlyField
from core.models import Estoque, MovimentacaoEstoque

class EstoqueSerializer(ModelSerializer):
    produto_nome = CharField(source='produto.nome', read_only=True)
    estoque_baixo = ReadOnlyField()
    estoque_alto = ReadOnlyField()
    
    class Meta:
        model = Estoque
        fields = '__all__'

class MovimentacaoEstoqueSerializer(ModelSerializer):
    produto_nome = CharField(source='produto.nome', read_only=True)
    usuario_nome = CharField(source='usuario.name', read_only=True)
    tipo_movimentacao_display = CharField(source='get_tipo_movimentacao_display', read_only=True)
    
    class Meta:
        model = MovimentacaoEstoque
        fields = '__all__'
