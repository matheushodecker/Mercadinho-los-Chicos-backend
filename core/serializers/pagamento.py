from rest_framework.serializers import ModelSerializer, CharField
from core.models import FormaPagamento, Pagamento

class FormaPagamentoSerializer(ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = '__all__'

class PagamentoSerializer(ModelSerializer):
    venda_numero = CharField(source='venda.numero_venda', read_only=True)
    forma_pagamento_nome = CharField(source='forma_pagamento.nome', read_only=True)
    status_display = CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Pagamento
        fields = '__all__'
