from rest_framework import viewsets
from .models import CentroCusto, ContaContabil
from .serializer import CentroCustoSerializer, ContaContabilSerializer
from .filters import CentroCustoFilter, ContaContabilFilter


class CentroCustoViewSet(viewsets.ModelViewSet):
    queryset = CentroCusto.objects.all()
    filterset_class = CentroCustoFilter
    serializer_class = CentroCustoSerializer


class ContaContabilViewSet(viewsets.ModelViewSet):
    queryset = ContaContabil.objects.all()
    filterset_class = ContaContabilFilter
    serializer_class = ContaContabilSerializer