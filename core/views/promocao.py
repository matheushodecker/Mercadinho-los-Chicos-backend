from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from core.models import Promocao
from core.serializers.promocao import PromocaoSerializer

class PromocaoViewSet(ModelViewSet):
    queryset = Promocao.objects.all()
    serializer_class = PromocaoSerializer
    
    @action(detail=False, methods=['get'])
    def promocoes_ativas(self, request):
        """Retorna promoções ativas no momento."""
        agora = timezone.now()
        promocoes = self.queryset.filter(
            ativo=True,
            data_inicio__lte=agora,
            data_fim__gte=agora
        )
        serializer = self.get_serializer(promocoes, many=True)
        return Response(serializer.data)
