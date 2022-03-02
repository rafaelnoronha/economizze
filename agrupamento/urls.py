from rest_framework.routers import SimpleRouter
from .views import CentroCustoViewSet, ContaContabilViewSet

router_centro_custo = SimpleRouter()
router_centro_custo.register('', CentroCustoViewSet)

router_conta_contabil = SimpleRouter()
router_conta_contabil.register('', ContaContabilViewSet)