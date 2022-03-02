import imp
from django.db import models
from base.models import Base


TIPO_CHOISES = [
    ('A', 'Analítico'),
    ('S', 'Sintético'),
]

class CentroCusto(Base):
    codigo = models.CharField(
        verbose_name='Código',
        max_length=15,
        help_text='Código do centro de custo ex: 1.101.1000',
    )

    descricao = models.CharField(
        verbose_name='Descrição',
        max_length=255,
        help_text='Descrição do centro de custo ex: Departamento Pessoal',
    )

    tipo = models.CharField(
        verbose_name='Tipo',
        choices=TIPO_CHOISES,
        max_length=1,
        help_text='Tipo do centro de custo do lançamento ex: A = Analítico ou S = Sintético',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'centro_custo'
        verbose_name = 'Centro de Custo'
        verbose_name_plural = 'Centro de Custos'

    def __str__(self):
        return f'({ self.id }) { self.codigo } - { self.descricao }'


class ContaContabil(Base):
    codigo = models.CharField(
        verbose_name='Código',
        max_length=15,
        help_text='Código da conta contábil ex: 2.202.2000',
    )

    descricao = models.CharField(
        verbose_name='Descrição',
        max_length=255,
        help_text='Descrição da conta contábil ex: Compra de materiais de escritório',
    )

    tipo = models.CharField(
        verbose_name='Tipo',
        choices=TIPO_CHOISES,
        max_length=1,
        help_text='Tipo da conta contábil do lançamento ex: A = Analítico ou S = Sintético',
    )

    class Meta:
        ordering = ['-id']
        db_table = 'conta_contabil'
        verbose_name = 'Conta Contábil'
        verbose_name_plural = 'Contas Contábeis'

    def __str__(self):
        return f'({ self.id }) { self.codigo } - { self.descricao }'
