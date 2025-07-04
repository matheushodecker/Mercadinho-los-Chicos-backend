from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import F
from core.models import Produto
from core.serializers.produto import ProdutoSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.filter(ativo=True)
    serializer_class = ProdutoSerializer
    
    @action(detail=False, methods=['get'])
    def estoque_baixo(self, request):
        """Retorna produtos com estoque baixo."""
        produtos = self.queryset.filter(estoque_atual__lte=F('estoque_minimo'))
        serializer = self.get_serializer(produtos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def buscar_por_codigo(self, request):
        """Busca produto por código de barras."""
        codigo = request.query_params.get('codigo')
        if codigo:
            try:
                produto = self.queryset.get(codigo_barras=codigo)
                serializer = self.get_serializer(produto)
                return Response(serializer.data)
            except Produto.DoesNotExist:
                return Response({'error': 'Produto não encontrado'}, status=404)
        return Response({'error': 'Código não informado'}, status=400)
