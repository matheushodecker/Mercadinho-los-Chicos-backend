from rest_framework.viewsets import ModelViewSet
from core.models import FormaPagamento, Pagamento
from core.serializers.pagamento import FormaPagamentoSerializer, PagamentoSerializer

class FormaPagamentoViewSet(ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer

class PagamentoViewSet(ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
