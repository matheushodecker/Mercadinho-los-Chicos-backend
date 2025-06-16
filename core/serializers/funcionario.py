from rest_framework.serializers import ModelSerializer, CharField
from core.models import Funcionario

class FuncionarioSerializer(ModelSerializer):
    cargo_nome = CharField(source='cargo.nome', read_only=True)
    
    class Meta:
        model = Funcionario
        fields = '__all__'
