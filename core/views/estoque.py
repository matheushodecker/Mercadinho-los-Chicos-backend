from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from core.models import Estoque, MovimentacaoEstoque
from core.serializers.estoque import EstoqueSerializer, MovimentacaoEstoqueSerializer

class EstoqueViewSet(ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    
    @action(detail=False, methods=['get'])
    def estoque_baixo(self, request):
        """Retorna produtos com estoque baixo."""
        estoques = self.queryset.filter(quantidade_atual__lte=models.F('quantidade_minima'))
        serializer = self.get_serializer(estoques, many=True)
        return Response(serializer.data)

class MovimentacaoEstoqueViewSet(ModelViewSet):
    queryset = MovimentacaoEstoque.objects.all()
    serializer_class = MovimentacaoEstoqueSerializer
