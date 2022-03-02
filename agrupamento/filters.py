from django_filters import rest_framework as filters
from .models import CentroCusto, ContaContabil


class CentroCustoFilter(filters.FilterSet):
    class Meta:
        model = CentroCusto
        fields = {
            'codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
            'descricao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
            'tipo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        }


class ContaContabilFilter(filters.FilterSet):
    class Meta:
        model = ContaContabil
        fields = {
            'codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
            'descricao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
            'tipo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
        }