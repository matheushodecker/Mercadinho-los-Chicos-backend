from rest_framework.serializers import ModelSerializer, CharField
from core.models import RelatorioVenda, RelatorioEstoque

class RelatorioVendaSerializer(ModelSerializer):
    usuario_gerador_nome = CharField(source='usuario_gerador.name', read_only=True)
    
    class Meta:
        model = RelatorioVenda
        fields = '__all__'

class RelatorioEstoqueSerializer(ModelSerializer):
    usuario_gerador_nome = CharField(source='usuario_gerador.name', read_only=True)
    
    class Meta:
        model = RelatorioEstoque
        fields = '__all__'
