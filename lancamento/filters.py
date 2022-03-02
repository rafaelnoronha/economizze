from django_filters import rest_framework as filters
from .models import Lancamento


class LancamentoFilter(filters.FilterSet):
    class Meta:
        model = Lancamento
        fields = {
            'descricao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
            'valor': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'range', 'gte', 'lte', 'gt', 'lt', ],
            'data': ['exact', 'range', 'year', 'year__gte', 'year__gt', 'year__lte', 'year__lt', 'year__range', 'year__in', 'month', 'month__gte', 'month__gt', 'month__lte', 'month__lt', 'month__range', 'month__in', 'day', 'day__gte', 'day__gt', 'day__lte', 'day__lt', 'day__range', 'day__in', 'gte', 'gt', 'lte', 'lt', 'in', ],
            'centro_custo': ['exact', ],
            'centro_custo__codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
            'centro_custo__descricao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
            'centro_custo__tipo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
            'conta_contabil': ['exact', ],
            'conta_contabil__codigo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
            'conta_contabil__descricao': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
            'conta_contabil__tipo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
            'tipo': ['exact', 'iexact', 'icontains', 'istartswith', 'iendswith', 'in', 'iregex', ],
            'baixado': ['exact', 'iregex', ],
        }
