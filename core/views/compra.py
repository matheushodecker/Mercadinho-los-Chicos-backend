from rest_framework.viewsets import ModelViewSet
from core.models import Compra
from core.serializers.compra import CompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
