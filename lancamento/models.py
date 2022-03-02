from django.db import models
from agrupamento.models import TIPO_CHOISES
from base.models import Base
from agrupamento.models import CentroCusto, ContaContabil

TIPO_CHOISES = [
    ('D', 'Débito'),
    ('C', 'Crédito'),
]


class Lancamento(Base):
    descricao = models.CharField(
        verbose_name='Descrição',
        max_length=255,
        help_text='Descrição do centro de custo ex: Departamento Pessoal',
    )

    valor = models.DecimalField(
        verbose_name='Valor',
        max_digits=11,
        decimal_places=2,
        help_text='Valor do lançamento',
    )

    data = models.DateField(
        verbose_name='Data do Lançamento',
        help_text='Data do lançamento da',
    )

    centro_custo = models.ForeignKey(
        CentroCusto,
        verbose_name='Centro de Custo',
        related_name='agrupamento_centro_custo_lancamento',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text='Centro de custo do lançamento',
    )

    conta_contabil = models.ForeignKey(
        ContaContabil,
        verbose_name='Conta Contábil',
        related_name='agrupamento_conta_contabil_lancamento',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text='Conta contábil do lançamento',
    )

    tipo = models.CharField(
        verbose_name='Tipo',
        choices=TIPO_CHOISES,
        max_length=1,
        help_text='Tipo do lancamento ex: D = Débito ou C = Crédito',
    )

    baixado = models.BooleanField(
        verbose_name='Baixado',
        default=False,
        help_text='Se o lançamento foi recebido/pago',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'lancamento'
        verbose_name = 'Lançamento'
        verbose_name_plural = 'Lançamentos'

    def __str__(self):
        return f'({ self.id }) { self.descricao } - R$ { self.valor }'
