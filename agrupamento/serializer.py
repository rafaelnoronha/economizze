from rest_framework import serializers
from .models import CentroCusto, ContaContabil


class CentroCustoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroCusto
        read_only_fields = [
            'uuid',
        ]
        fields = '__all__'


class ContaContabilSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContaContabil
        read_only_fields = [
            'uuid',
        ]
        fields = '__all__'