from rest_framework.viewsets import ModelViewSet
from core.models import Cargo
from core.serializers.cargo import CargoSerializer

class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
