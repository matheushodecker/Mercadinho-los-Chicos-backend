from rest_framework.serializers import ModelSerializer, CharField
from core.models import Venda, ItemVenda

class ItemVendaSerializer(ModelSerializer):
    produto_nome = CharField(source='produto.nome', read_only=True)
    
    class Meta:
        model = ItemVenda
        fields = ['id', 'produto', 'produto_nome', 'quantidade', 'preco_unitario', 'subtotal']

class VendaSerializer(ModelSerializer):
    itens = ItemVendaSerializer(many=True, read_only=True)
    usuario_nome = CharField(source='usuario.name', read_only=True)
    
    class Meta:
        model = Venda
        fields = [
            'id', 'usuario', 'usuario_nome', 'data_venda', 'total',
            'desconto', 'status', 'observacoes', 'itens'
        ]
