from rest_framework import serializers
from .models import Lancamento
from agrupamento.serializer import CentroCustoSerializer, ContaContabilSerializer


class LancamentoSerializer(serializers.ModelSerializer):
    centro_custo = CentroCustoSerializer(read_only=True)
    conta_contabil = ContaContabilSerializer(read_only=True)

    class Meta:
        model = Lancamento
        fields = '__all__'


class LancamentoSerializerPostPutPatch(serializers.ModelSerializer):
    class Meta:
        model = Lancamento
        read_only_fields = [
            'uuid',
        ]
        fields = '__all__'