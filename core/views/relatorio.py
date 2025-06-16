from rest_framework.viewsets import ModelViewSet
from core.models import RelatorioVenda, RelatorioEstoque
from core.serializers.relatorio import RelatorioVendaSerializer, RelatorioEstoqueSerializer

class RelatorioVendaViewSet(ModelViewSet):
    queryset = RelatorioVenda.objects.all()
    serializer_class = RelatorioVendaSerializer

class RelatorioEstoqueViewSet(ModelViewSet):
    queryset = RelatorioEstoque.objects.all()
    serializer_class = RelatorioEstoqueSerializer
