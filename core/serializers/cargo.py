from rest_framework.serializers import ModelSerializer
from core.models import Cargo

class CargoSerializer(ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'
