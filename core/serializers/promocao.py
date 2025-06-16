from rest_framework.serializers import ModelSerializer, CharField, ReadOnlyField
from core.models import Promocao, ProdutoPromocao

class ProdutoPromocaoSerializer(ModelSerializer):
    produto_nome = CharField(source='produto.nome', read_only=True)
    promocao_nome = CharField(source='promocao.nome', read_only=True)
    
    class Meta:
        model = ProdutoPromocao
        fields = '__all__'

class PromocaoSerializer(ModelSerializer):
    produtos = ProdutoPromocaoSerializer(many=True, read_only=True)
    tipo_desconto_display = CharField(source='get_tipo_desconto_display', read_only=True)
    promocao_ativa = ReadOnlyField()
    
    class Meta:
        model = Promocao
        fields = '__all__'
