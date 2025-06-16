from rest_framework.serializers import ModelSerializer, CharField
from core.models import Compra, ItemCompra

class ItemCompraSerializer(ModelSerializer):
    produto_nome = CharField(source='produto.nome', read_only=True)
    
    class Meta:
        model = ItemCompra
        fields = '__all__'

class CompraSerializer(ModelSerializer):
    fornecedor_nome = CharField(source='fornecedor.nome', read_only=True)
    usuario_nome = CharField(source='usuario.name', read_only=True)
    itens = ItemCompraSerializer(many=True, read_only=True)
    status_display = CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Compra
        fields = '__all__'
