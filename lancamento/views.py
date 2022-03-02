from rest_framework import viewsets
from .models import Lancamento
from .serializer import LancamentoSerializer, LancamentoSerializerPostPutPatch
from .filters import LancamentoFilter


class LancamentoViewSet(viewsets.ModelViewSet):
    queryset = Lancamento.objects.all()
    filterset_class = LancamentoFilter

    serializer_classes = {
        'create': LancamentoSerializerPostPutPatch,
        'update': LancamentoSerializerPostPutPatch,
        'partial_update': LancamentoSerializerPostPutPatch,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, LancamentoSerializer)