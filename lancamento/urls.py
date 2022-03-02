from rest_framework.routers import SimpleRouter
from .views import LancamentoViewSet

router_lancamento = SimpleRouter()
router_lancamento.register('', LancamentoViewSet)
